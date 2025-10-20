import base64
import json
import os
import re
import uuid

import cloudinary
import cloudinary.uploader
from flask import current_app as app
from flask import Blueprint, jsonify, request
from model import Character, Image, db
from services.openrouter import OpenrouterService
from utils.images import image_to_base64

character_bp = Blueprint("character_bp", __name__)


"""
@DELETE /API/CHARACTER

Delete character 
"""


@character_bp.delete("")
def delete_character():
    app.logger.info("[In @DELETE/API/CHARACTER route]")

    character_id = request.args.get("character_id")

    stmt = (
        db.delete(Character)
        .where(Character.id == character_id)
        .returning(
            Character.id,
            Character.name,
            Character.description,
            Character.ability1,
            Character.ability2,
            Character.ability1_description,
            Character.ability2_description,
            Character.alignment,
            Character.faction,
            Character.attack,
            Character.defense,
            Character.speed,
            Character.luck,
            Character.image,
        )
    )
    row = db.session.execute(stmt).one_or_none()
    if row is None:
        return jsonify({"msg": "Character not found"}), 404
    db.session.commit()

    return "success", 200


"""
@GET /API/CHARACTER

Get character 
"""


@character_bp.get("")
def get_character():
    app.logger.info("[In @GET/API/CHARACTER route]")

    character_id = request.args.get("character_id")

    stmt = db.select(Character).where(Character.id == character_id)
    character = db.session.execute(stmt).scalars().one()

    if not character:
        return jsonify({"character": [], "msg": "Character doesn't exist"}), 500

    payload = {
        "id": character.id,
        "name": character.name,
        "description": character.description,
        "ability1": character.ability1,
        "ability2": character.ability2,
        "ability1_description": character.ability1_description,
        "ability2_description": character.ability2_description,
        "alignment": character.alignment,
        "faction": character.faction,
        "attack": character.attack,
        "defense": character.defense,
        "speed": character.speed,
        "luck": character.luck,
        "image": {
            "id": character.image.id if character.image else None,
            "name": character.image.name if character.image else None,
            "hash": character.image.hash if character.image else None,
        },
    }

    return jsonify({"character": payload}), 200


"""
@POST /API/CHARACTER

Create character 
"""


@character_bp.post("")
def create_character():
    app.logger.info("[In @POST/API/CHARACTER route]")
    app.logger.info(f"Request files: {list(request.files.keys())}")

    if request.method == "POST":
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        )

        upload_result = None

        # Get file from request
        file_to_upload = request.files["file"]
        app.logger.info("%s file_to_upload", file_to_upload.filename)

        # Verify if image already exists by its name
        existing = db.session.execute(
            db.select(Image).filter_by(name=file_to_upload.filename)
        ).scalar_one_or_none()

        if existing:
            app.logger.info("Image already exists: %s", existing.id)
            image_hash = existing.hash
            image_id = existing.id
            image_base64 = image_to_base64(image_hash)
        else:
            # Upload image to cloudinary
            if not file_to_upload:
                return "File not found", 500
            upload_result = cloudinary.uploader.upload(
                file_to_upload,
                folder="flask_app_uploads/",
                public_id=file_to_upload.filename,
                display_name=file_to_upload.filename,
            )
            app.logger.info(upload_result)

            # Store image hash in db
            image = Image()
            image_id = str(uuid.uuid4())
            image.id = image_id
            image_hash = upload_result["secure_url"]
            image.hash = image_hash
            image.name = (
                file_to_upload.filename
                or upload_result.get("display_name")
                or str(uuid.uuid4())
            )
            db.session.add(image)
            db.session.commit()

            # Decode image for sending to LLM
            file_to_upload.stream.seek(0)
            image_bytes = file_to_upload.read()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        # Query LLM for character info
        app.logger.info("Querying LLM for character info")
        # ollama = OllamaService(host="http://ollama:11434")
        # res_raw = ollama.query(
        #     "Create a JSON object containing: name: (Name of that character), description: (Description of that character), ability1: (First ability of character), ability2: (Second ability of character), ability1_description: (Description of ability 1), ability2_description: (Description of ability 2)",
        #     "Your goal is to generate characters card based on the image provided. Respond ONLY with valid JSON, no markdown formatting. Do not make the field too long",
        #     image_base64,
        # )
        openrouter = OpenrouterService()
        res_raw = openrouter.query(
            """
            Return ONLY one JSON object (no markdown).

            REQUIRED (13) keys in this exact order:
            name, description, ability1, ability2, ability1_description, ability2_description,
            alignment, faction, attack, defense, speed, luck

            Rules:
            1. Do not omit, rename, or add keys.
            2. Use short, game-card length values (≤ 120 chars per description).
            3. Numbers: integers 0–100 (attack/defense/speed/luck).
            4. If unsure, make a best-fit guess (never use “N/A”).
            5. Before responding, verify all 13 keys are present.

            JSON skeleton to fill (respond with this filled in):
            {
                "name": "",
                "description": "",
                "ability1": "",
                "ability2": "",
                "ability1_description": "",
                "ability2_description": "",
                "alignment": "",
                "faction": "",
                "attack": 0,
                "defense": 0,
                "speed": 0,
                "luck": 0
            }
            """,
            image_hash,
        )

        app.logger.info(upload_result)

        # Format LLM output into json
        res_cleaned = re.sub(r"```json\n?|\n?```", "", res_raw).strip()
        try:
            character_data = json.loads(res_cleaned)
        except json.JSONDecodeError as e:
            app.logger.error(f"JSON decode error: {e}")
            return jsonify({"error": "Failed to parse LLM response"}), 500

        # Add the character to the db
        character = Character()
        character.id = str(uuid.uuid4())
        character.name = character_data["name"] or ""
        character.description = character_data["description"] or res_raw
        character.ability1 = character_data["ability1"] or res_raw
        character.ability2 = character_data["ability2"] or res_raw
        character.ability1_description = (
            character_data["ability1_description"] or res_raw
        )
        character.ability2_description = (
            character_data["ability2_description"] or res_raw
        )
        character.alignment = character_data["alignment"]
        character.faction = character_data["faction"]
        character.attack = int(character_data["attack"]) or 0
        character.defense = int(character_data["defense"]) or 0
        character.speed = int(character_data["speed"]) or 0
        character.luck = int(character_data["luck"]) or 0
        character.image_id = image_id
        app.logger.info(character_data)
        db.session.add(character)
        db.session.commit()

        return jsonify(
            {
                "msg": "success",
                "character": {
                    "id": character.id,
                    "name": character.name,
                    "description": character.description,
                    "ability1": character.ability1,
                    "ability2": character.ability2,
                    "ability1_description": character.ability1_description,
                    "ability2_description": character.ability2_description,
                    "alignment": character.alignment,
                    "faction": character.faction,
                    "attack": character.attack,
                    "defense": character.defense,
                    "speed": character.speed,
                    "luck": character.luck,
                    "image": {
                        "id": character.image.id if character.image else None,
                        "name": character.image.name if character.image else None,
                        "hash": character.image.hash if character.image else None,
                    },
                },
            }
        ), 200

    return "Request method invalid", 405

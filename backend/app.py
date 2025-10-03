import os
import uuid
import base64
import json
import re

import cloudinary
import cloudinary.uploader
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import Character, Image, db
from services.ollama import OllamaService


load_dotenv()

app = Flask(__name__)

# Configure ORM

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

# Configure CORS

CORS(app)

with app.app_context():
    db.create_all()


def get_db_connection():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    return conn


@app.route("/api/hello")
def hello():
    return jsonify({"msg": "test"})


"""
@POST /API/IMAGE

Receive image, store it into the cloud with cloudinary and add it's hash to the db.
"""


@app.post("/api/image")
def upload_file():
    app.logger.info("[In /api/upload route]")
    app.logger.info(f"Request files: {list(request.files.keys())}")

    # Store image in cloudinary

    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )

    upload_result = None

    if request.method == "POST":
        file_to_upload = request.files["file"]
        app.logger.info("%s file_to_upload", file_to_upload.name)

        # Attempt to upload file to cloud
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(
                file_to_upload, folder="flask_app_uploads/"
            )
        else:
            return "File not found", 500
        app.logger.info(upload_result)

        # Store image hash in db
        image = Image()
        image_id = str(uuid.uuid4())
        image.id = image_id
        image.hash = upload_result["secure_url"]
        db.session.add(image)
        db.session.commit()

        return jsonify(
            {"msg": "success", "id": image_id, "hash": upload_result["secure_url"]}
        ), 200

    return "Request method invalid", 405


"""
@POST /API/CHARACTER

Create character 
"""


@app.post("/api/character")
def create_character():
    app.logger.info("[In /api/character route]")
    app.logger.info(f"Request files: {list(request.files.keys())}")

    if request.method == "POST":
        # Store image in cloudinary

        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
        )

        upload_result = None

        file_to_upload = request.files["file"]
        app.logger.info("%s file_to_upload", file_to_upload.name)

        if file_to_upload:
            upload_result = cloudinary.uploader.upload(
                file_to_upload, folder="flask_app_uploads/"
            )
        else:
            return "File not found", 500
        app.logger.info(upload_result)

        # Store image hash in db

        image = Image()
        image_id = str(uuid.uuid4())
        image.id = image_id
        image.hash = upload_result["secure_url"]
        db.session.add(image)
        db.session.commit()

        # Query LLM for character info
        file_to_upload.stream.seek(0)
        image_bytes = file_to_upload.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        ollama = OllamaService(host="http://ollama:11434")
        res_raw = ollama.query(
            "Create a JSON object containing: name (Name of that character), (Description of that character)",
            "Your goal is to generate characters card based on the image provided. Respond ONLY with valid JSON, no markdown formatting.",
            image_base64,
        )

        app.logger.info(upload_result)

        # Add the character to the db
        res_cleaned = re.sub(r"```json\n?|\n?```", "", res_raw).strip()
        try:
            character_data = json.loads(res_cleaned)
        except json.JSONDecodeError as e:
            app.logger.error(f"JSON decode error: {e}")
            return jsonify({"error": "Failed to parse LLM response"}), 500
        character = Character()
        character.id = character_id = str(uuid.uuid4())
        character.name = character_data["name"] or ""
        character.description = character_data["description"] or res_raw
        app.logger.info(character)
        db.session.add(character)
        db.session.commit()

        return jsonify(
            {
                "msg": "success",
                "res": res_raw,
                "id": image_id,
                "hash": upload_result["secure_url"],
            }
        ), 200

    return "Request method invalid", 405


@app.route("/api/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables LIMIT 5;")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"tables": tables})

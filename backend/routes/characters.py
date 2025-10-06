from flask import current_app as app
from flask import Blueprint, jsonify
from model import Character, Image, db

characters_bp = Blueprint("characters_bp", __name__)


"""
@GET /API/CHARACTERS

Get characters 
"""


@characters_bp.get("")
def get_characters():
    app.logger.info("[In @GET /api/characters route]")

    stmt = db.select(Character).order_by(Character.name)
    result = db.session.execute(stmt).scalars().all()

    if not result:
        return jsonify({"characters": [], "msg": "no characters found"}), 200

    payload = []
    for c in result:
        payload.append(
            {
                "id": c.id,
                "name": c.name,
                "description": c.description,
                "ability1": c.ability1,
                "ability2": c.ability2,
                "ability1_description": c.ability1_description,
                "ability2_description": c.ability2_description,
                "image": {
                    "id": c.image.id if c.image else None,
                    "name": c.image.name if c.image else None,
                    "hash": c.image.hash if c.image else None,
                },
            }
        )

    return jsonify({"characters": payload}), 200

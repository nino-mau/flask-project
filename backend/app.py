import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from model import db
from routes.character import character_bp
from routes.characters import characters_bp
from routes.character.export import export_bp
from cloudsql_connect import get_engine

load_dotenv()

app = Flask(__name__)

engine = get_engine()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+pg8000://"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"creator": engine.pool._creator}
db.init_app(app)

CORS(app)

with app.app_context():
    db.create_all()


# Register routes

app.register_blueprint(character_bp, url_prefix="/api/character")

app.register_blueprint(characters_bp, url_prefix="/api/characters")

app.register_blueprint(export_bp, url_prefix="/api/character/export")

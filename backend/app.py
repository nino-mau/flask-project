import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from model import db
from routes.character import character_bp
from routes.characters import characters_bp
from routes.character.export import export_bp

load_dotenv()

app = Flask(__name__)

# Configure app

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db.init_app(app)

CORS(app)

with app.app_context():
    db.create_all()


def get_db_connection():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    return conn


# Register routes

app.register_blueprint(character_bp, url_prefix="/api/character")

app.register_blueprint(characters_bp, url_prefix="/api/characters")

app.register_blueprint(export_bp, url_prefix="/api/character/export")

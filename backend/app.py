from flask import Flask, jsonify, request
from flask_cors import CORS
from ollama import Client
from dotenv import load_dotenv
import psycopg2, os, cloudinary, cloudinary.uploader, json

load_dotenv()

ollama_model = os.getenv("OLLAMA_MODEL") or "gemma:2b-instruct-q4_K_M"

app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    return conn


@app.route("/api/hello")
def hello():
    ollama_client = Client(host="http://ollama:11434")

    res = ollama_client.chat(
        model=ollama_model,
        messages=[{"role": "user", "content": "Hello, explain AI in 2 sentences."}],
    )

    return jsonify({"msg": res["message"]["content"]})


@app.post("/api/upload")
def upload_file():
    app.logger.info("[In /api/upload route]")
    app.logger.info(f"Request files: {list(request.files.keys())}")
    cloudinary.config(
        cloud_name=os.getenv("CLOUDINARY_NAME"),
        api_key=os.getenv("CLOUDINARY_API_KEY"),
        api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    )

    upload_result = None
    if request.method == "POST":
        file_to_upload = request.files["file"]
        app.logger.info("%s file_to_upload", file_to_upload)
        if file_to_upload:
            upload_result = cloudinary.uploader.upload(
                file_to_upload, folder="flask_project_uploads/"
            )
        app.logger.info(upload_result)
        return jsonify(upload_result)
    return jsonify({"msg": "Should be a post request"})


@app.route("/api/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables LIMIT 5;")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"tables": tables})

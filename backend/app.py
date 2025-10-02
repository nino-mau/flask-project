from flask import Flask, jsonify
from flask_cors import CORS
from ollama import Client
from dotenv import load_dotenv
import psycopg2, os, json, requests

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


@app.route("/api/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables LIMIT 5;")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({"tables": tables})

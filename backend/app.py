from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route("/")
def home():
    return jsonify({"message": "API running OK"})

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Thanh"},
        {"id": 2, "name": "Docker"}
    ])

@app.route("/db")
def test_db():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode="require")
        conn.close()
        return jsonify({"status": "Connected to Render DB"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
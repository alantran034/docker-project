from flask import Flask, jsonify, request
from db import get_conn
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "🚀 Docker Cloud OK"})

@app.route("/init-db")
def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

    return "DB initialized"

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users ORDER BY id;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([{"id": r[0], "name": r[1]} for r in rows])

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name) VALUES (%s) RETURNING id;",
        (data["name"],)
    )

    new_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": new_id})

@app.route("/db")
def test_db():
    try:
        conn = get_conn()
        conn.close()
        return jsonify({"status": "DB OK"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
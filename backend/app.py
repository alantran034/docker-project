from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database="postgres",
        user="postgres",
        password="postgres"
    )
    return conn

@app.route("/")
def home():
    return jsonify({"message": "Backend is running 🚀"})

@app.route("/data")
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify({"time": str(result[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
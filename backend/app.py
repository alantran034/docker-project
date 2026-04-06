from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            os.environ.get("postgresql://postgres1:FSHxbpNTO2K3TOYQ44RDUXD0XbqYL0be@dpg-d79ukln5r7bs738376ag-a/postgres1_5b72")
        )
        return conn
    except Exception as e:
        print(" Lỗi kết nối DB:", e)
        return None


@app.route("/")
def home():
    return "Docker Project chạy OK 🚀"


@app.route("/data")
def data():
    conn = get_db_connection()

    if conn is None:
        return jsonify({
            "status": "error",
            "message": "Không kết nối được database"
        })

    try:
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()

        cur.close()
        conn.close()

        return jsonify({
            "status": "success",
            "time": str(result[0])
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
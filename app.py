import os
import mysql.connector
from flask import Flask, jsonify

from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)

@app.route("/")
def index():
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = db.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    return jsonify({
        "message": "Flask + MySQL Docker Compose Setup Success",
        "db_test": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("DEBUG", False))

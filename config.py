import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv(override=True)

# Set default values for environment variables (in docker container)
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = os.getenv("FLASK_PORT", "5000")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
DB_HOST = os.getenv(
    "DB_HOST", "db"
)  # Default to db if not set in the docker-compose file
DB_PORT = os.getenv(
    "DB_PORT", "3306"
)  # Default to 3306 if not set in the docker-compose file
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy()
db.init_app(app)

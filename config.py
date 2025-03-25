import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(override=True)

FLASK_HOST = os.getenv("FLASK_HOST", "localhost")
FLASK_HOST_PORT = os.getenv("FLASK_HOST_PORT", "5001")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")  # Default to localhost if not set
DB_PORT = os.getenv("DB_PORT", "3306")  # Default to 3306 if not set
DB_NAME = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

SQLALCHEMY_TRACK_MODIFICATIONS = False

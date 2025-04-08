import os

from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()  # Load biến từ .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_BLACKLIST_ENABLED = True

    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY",)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


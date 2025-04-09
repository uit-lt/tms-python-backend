import os

from dotenv import load_dotenv
from datetime import timedelta

from config import SQLALCHEMY_DATABASE_URI

load_dotenv()  # Load define variable in .env

class Config:
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI

    # JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_BLACKLIST_ENABLED = True

    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY",)

    SQLALCHEMY_TRACK_MODIFICATIONS = False


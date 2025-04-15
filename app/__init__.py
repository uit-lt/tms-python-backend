from flask import Flask
from app.helpers.extensions import db, migrate, ma

from app.routes import main_bp
from app.tasks.routes import tasks_bp
from app.users.routes import users_bp
from config import SQLALCHEMY_DATABASE_URI
from flask_jwt_extended import JWTManager

jwt = JWTManager()

def create_app(test_config=None):
    app = Flask(__name__)

    # Configure your app
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)

    return app
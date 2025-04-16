from flasgger import Swagger
from flask import Flask
from app.auth import auth_bp
from app.config import Config
from app.helpers.extensions import init_extensions

from app.routes import main_bp
from app.tasks.routes import tasks_bp
from app.users.routes import users_bp


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)
    init_extensions(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Task Management API",
        "description": "API for user registration, login, and task management.",
        "version": "1.0"
    },
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
        }
    },
    "security": [{"BearerAuth": []}]
    }
    Swagger(app, template=swagger_template)

    return app

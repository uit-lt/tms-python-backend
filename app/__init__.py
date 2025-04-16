from flask import Flask
from app.auth import auth_bp
from app.config import Config
from app.helpers.extensions import init_extensions  # CHỈ cần import hàm này

from app.routes import main_bp
from app.tasks.routes import tasks_bp
from app.users.routes import users_bp

jwt = JWTManager()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    init_extensions(app)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    return app
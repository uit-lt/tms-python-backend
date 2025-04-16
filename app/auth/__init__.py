from flask import Flask

from app.config import Config
from app.helpers.extensions import db, jwt
from flask_migrate import Migrate
from app.auth.routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)

    app.register_blueprint(auth_bp)

    return app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta

from app.helpers.jwt_blocklist import jwt_blocklist

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()

def init_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)

@jwt.token_in_blocklist_loader
def check_if_token_revoked(_unused, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in jwt_blocklist
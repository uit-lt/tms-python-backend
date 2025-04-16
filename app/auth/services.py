from app.helpers.jwt_blocklist import jwt_blocklist
from app.helpers.validators import is_valid_email, is_strong_password
from app.models import User
from app.helpers.extensions import db
from werkzeug.security import generate_password_hash

def create_user(data):
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')

    if not username or not email or not password:
        return "Username, email and password are required.", 400

    if username == "" or email == "":
        return "Username and email must not be empty or spaces only.", 400

    if not is_valid_email(email):
        return "Invalid email format.", 400

    if not is_strong_password(password):
        return (
            "Password must be at least 8 characters and include "
            "uppercase, lowercase, number, and special character.",
            400
        )

    if User.query.filter_by(username=username).first():
        return "Username already exists.", 400

    if User.query.filter_by(email=email).first():
        return "Email already exists.", 400

    new_user = User(
        username=username,
        email=email,
        password_hash=generate_password_hash(password)
    )
    db.session.add(new_user)
    db.session.commit()
    return "User created successfully", 201

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in jwt_blocklist
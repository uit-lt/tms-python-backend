from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.auth.services import create_user, get_user_by_email, get_user_by_id, jwt_blocklist
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# GET METHODS
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()
    user = get_user_by_id(int(user_id))

    if not user:
        return jsonify(message="User not found"), 404

    return jsonify(
        id=user.id,
        username=user.username,
        email=user.email
    ), 200


# POST METHODS
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, status = create_user(data)
    return jsonify(message=result), status


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = get_user_by_email(data.get('email'))
    if user and check_password_hash(user.password_hash, data.get('password')):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token), 200

    return jsonify(message='Invalid credentials'), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    exp = get_jwt()["exp"]
    jwt_blocklist[jti] = exp
    return jsonify(message="Logged out"), 200
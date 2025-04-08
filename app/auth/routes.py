from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from app.auth.services import create_user, get_user_by_email
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

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
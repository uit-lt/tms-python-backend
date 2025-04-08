from flask import request, jsonify
from app.auth.services import create_user
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# POST METHODS
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, status = create_user(data)
    return jsonify(message=result), status


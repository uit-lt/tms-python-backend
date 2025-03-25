from flask import Blueprint

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users")
def get_users():
    return "List of users"

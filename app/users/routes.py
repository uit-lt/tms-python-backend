from flask import Blueprint, request, jsonify

users_bp = Blueprint("users_bp", __name__)

@users_bp.route("/users", methods=["GET"])
def get_tasks():
    return {"message": "Users list"}

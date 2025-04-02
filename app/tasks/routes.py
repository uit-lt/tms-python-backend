from flask import Blueprint, request, jsonify

tasks_bp = Blueprint("tasks_bp", __name__)

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return {"message": "Tasks list"}

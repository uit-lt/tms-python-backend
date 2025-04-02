from flask import Blueprint, request, jsonify

task_bp = Blueprint("task_bp", __name__)

@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    return {"message": "Tasks list"}

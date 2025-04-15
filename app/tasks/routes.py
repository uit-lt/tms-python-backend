from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import get_all_tasks, create_task, update_task, delete_task

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.route("/", methods=["GET"])
@jwt_required()
def list_tasks():
    current_user_id = get_jwt_identity()
    return jsonify(get_all_tasks(current_user_id))


@tasks_bp.route("/", methods=["POST"])
@jwt_required()
def post_task():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    return create_task(data, current_user_id)


@tasks_bp.route("/<int:task_id>", methods=["PUT"])
@jwt_required()
def put_task(task_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    return update_task(task_id, data, current_user_id)


@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task_route(task_id):
    current_user_id = get_jwt_identity()
    return delete_task(task_id, current_user_id)
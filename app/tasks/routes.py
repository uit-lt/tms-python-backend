from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

task_bp = Blueprint("task_bp", __name__)


@task_bp.route("/", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify(
        [
            {"id": task.id, "title": task.title, "completed": task.completed}
            for task in tasks
        ]
    )


@task_bp.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], user_id=data["user_id"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201

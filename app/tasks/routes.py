from flask import Blueprint, request, jsonify
from app import db
from app.models import Task

tasks = Blueprint("tasks", __name__)


@tasks.route('/')
def index():
    return "Tasks Home"

@tasks.route("/", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(title=data["title"], user_id=data["user_id"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201

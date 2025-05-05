from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import get_all_tasks, create_task, update_task, delete_task

tasks_bp = Blueprint("tasks_bp", __name__, url_prefix="/tasks")

@tasks_bp.route("/list_tasks", methods=["GET"])
@jwt_required()
def list_tasks():
    """
    Get tasks filtered by assignee or unassigned
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    produces:
      - application/json
    parameters:
      - name: assignee_id
        in: query
        type: integer
        required: false
        description: If provided, only return tasks assigned to this user. If not, return unassigned tasks.
    responses:
      200:
        description: List of tasks
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              title:
                type: string
              description:
                type: string
              status:
                type: string
              est_time:
                type: integer
              due_date:
                type: string
              priority:
                type: string
              assignee_id:
                type: integer
              project_id:
                type: integer
              created_by:
                type: integer
              created_at:
                type: string
              updated_at:
                type: string
    """
    current_user_id = get_jwt_identity()
    assignee_id = request.args.get("assignee_id", type=int)
    return jsonify(get_all_tasks(current_user_id, assignee_id))


@tasks_bp.route("/create_task_view", methods=["POST"])
@jwt_required()
def create_task_view():
    """
    Create a new task
    ---
    tags:
      - Tasks
    consumes:
      - application/json
    security:
      - BearerAuth: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - title
          properties:
            title:
              type: string
              example: Write report
            description:
              type: string
              example: Weekly project report
            assignee_id:
              type: integer
              example: 1
            project_id:
              type: integer
              example: 1
            status:
              type: string
              example: In Progress
            est_time:
              type: integer
              example: 5
            due_date:
              type: string
              format: date-time
              example: "2025-04-20T10:00:00"
    responses:
      201:
        description: Task created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            message:
              type: string
      400:
        description: Invalid input
    """
    current_user_id = get_jwt_identity()
    data = request.get_json()
    return create_task(data, current_user_id)


@tasks_bp.route("/update_task_view/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task_view(task_id):
    """
    Update an existing task
    ---
    tags:
      - Tasks
    consumes:
      - application/json
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: task_id
        required: true
        type: integer
        description: ID of the task to update
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Update title
            description:
              type: string
              example: Revised task description
            assignee_id:
              type: integer
              example: 1
    responses:
      200:
        description: Task updated successfully
        schema:
          type: object
          properties:
            id:
              type: integer
            title:
              type: string
            description:
              type: string
      404:
        description: Task not found
    """
    current_user_id = get_jwt_identity()
    data = request.get_json()
    return update_task(task_id, data, current_user_id)


@tasks_bp.route("/delete_task_view/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task_view(task_id):
    """
    Delete a task by ID
    ---
    tags:
      - Tasks
    security:
      - BearerAuth: []
    produces:
      - application/json
    parameters:
      - in: path
        name: task_id
        required: true
        type: integer
        description: ID of the task to delete
    responses:
      204:
        description: Task deleted successfully (no content)
      404:
        description: Task not found
    """
    current_user_id = get_jwt_identity()
    return delete_task(task_id, current_user_id)
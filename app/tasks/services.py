from app.models import Task
from app.helpers.extensions import db
from datetime import datetime

def create_task(data, user_id):
    due_date = data.get("due_date")
    if due_date:
        try:
            due_date = datetime.fromisoformat(due_date)
        except ValueError:
            return {"message": "Invalid due_date format. Must be ISO 8601."}, 400
    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "To Do"),
        est_time=data.get("est_time"),
        due_date=due_date,
        priority=data.get("priority"),
        assignee_id=data.get("assignee_id"),
        project_id=data.get("project_id"),
        created_by=user_id
    )
    db.session.add(task)
    db.session.commit()
    return {"message": "Task created", "id": task.id}, 201

def get_all_tasks(current_user_id, assignee_id=None):
    if assignee_id:
        tasks = Task.query.filter_by(assignee_id=assignee_id).all()
    else:
        tasks = Task.query.filter_by(assignee_id=None).all()

    return [{
        "id": t.id,
        "title": t.title,
        "description": t.description,
        "status": t.status,
        "est_time": t.est_time,
        "due_date": t.due_date.isoformat() if t.due_date else None,
        "priority": t.priority,
        "assignee_id": t.assignee_id,
        "project_id": t.project_id,
        "created_by": t.created_by,
        "created_at": t.created_at.isoformat(),
        "updated_at": t.updated_at.isoformat()
    } for t in tasks]

def update_task(task_id, data, user_id):
    user_id = int(user_id)

    task = Task.query.get_or_404(task_id)

    if task.created_by != user_id:
        return {"message": "Permission denied"}, 403

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)

    # Handle due_date
    due_date = data.get("due_date")
    if due_date:
        try:
            due_date = datetime.fromisoformat(due_date)
            task.due_date = due_date
        except ValueError:
            return {"message": "Invalid due_date format. Must be ISO 8601."}, 400

    task.priority = data.get("priority", task.priority)

    if "assignee_id" in data:
        task.assignee_id = data["assignee_id"]

    db.session.commit()
    return {"message": "Task updated"}, 200

def delete_task(task_id, user_id):
    user_id = int(user_id)

    print(type(user_id))
    task = Task.query.get_or_404(task_id)
  
    print(type(task.created_by))
    if task.created_by != user_id:
        return {"message": "Permission denied"}, 403

    db.session.delete(task)
    db.session.commit()
    return {"message": "Task deleted"}, 200

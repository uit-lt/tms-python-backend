from app.models import Task
from app.helpers.extensions import db

def create_task(data, user_id):
    task = Task(
        title=data["title"],
        description=data.get("description"),
        status=data.get("status", "To Do"),
        est_time=data.get("est_time"),
        due_date=data.get("due_date"),
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
        "status": t.status,
        "due_date": t.due_date.isoformat() if t.due_date else None
    } for t in tasks]

def update_task(task_id, data, user_id):
    user_id = int(user_id)

    task = Task.query.get_or_404(task_id)
  
    if task.created_by != user_id:
        return {"message": "Permission denied"}, 403

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.status = data.get("status", task.status)
    task.due_date = data.get("due_date", task.due_date)
    task.priority = data.get("priority", task.priority)
    task.assignee_id = data.get("assignee_id", task.priority)

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

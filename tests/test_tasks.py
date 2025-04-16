import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask_jwt_extended import create_access_token
from app.helpers.extensions import db
from app.models import User, Task, Project
from datetime import datetime


@pytest.fixture
def client():
    from app import create_app

    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            user1 = User(id=1, username="user1", email="u1@example.com", password_hash="hashed")
            user2 = User(id=2, username="user2", email="u2@example.com", password_hash="hashed")
            project = Project(id=1, name="Demo Project", description="Demo", created_by=1)

            db.session.add_all([user1, user2, project])
            db.session.commit()

        yield client

@pytest.fixture
def auth_headers_user1(client):
    with client.application.app_context():
        token = create_access_token(identity="1")
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def auth_headers_user2(client):
    with client.application.app_context():
        token = create_access_token(identity="2")
    return {"Authorization": f"Bearer {token}"}

def test_create_task(client, auth_headers_user1):
    res = client.post("/tasks/create_task_view", json={
        "title": "Task from test",
        "description": "Testing task creation",
        "assignee_id": 1,
        "project_id": 1,
        "due_date": datetime.utcnow().isoformat()
    }, headers=auth_headers_user1)

    assert res.status_code == 201
    assert res.json["message"] == "Task created"

def test_get_tasks(client, auth_headers_user1):
    client.post("/tasks/create_task_view", json={
        "title": "Another task",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)

    res = client.get("/tasks/list_tasks?assignee_id=1", headers=auth_headers_user1)
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert len(res.json) > 0

def test_update_task(client, auth_headers_user1):
    res = client.post("/tasks/create_task_view", json={
        "title": "Temp",
        "description": "Test",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    res = client.put(f"/tasks/update_task_view/{task_id}", json={
        "title": "Updated title",
        "description": "Updated desc"
    }, headers=auth_headers_user1)
    assert res.status_code == 200
    assert res.json["message"] == "Task updated"

def test_delete_task(client, auth_headers_user1):
    res = client.post("/tasks/create_task_view", json={
        "title": "To be deleted",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    res = client.delete(f"/tasks/delete_task_view/{task_id}", headers=auth_headers_user1)
    assert res.status_code == 200
    assert res.json["message"] == "Task deleted"

def test_forbidden_delete_other_users_task(client, auth_headers_user1, auth_headers_user2):
    res = client.post("/tasks/create_task_view", json={
        "title": "Secret",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    res = client.delete(f"/tasks/delete_task_view/{task_id}", headers=auth_headers_user2)
    assert res.status_code == 403
    assert res.json["message"] == "Permission denied"
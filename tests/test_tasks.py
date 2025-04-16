import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask_jwt_extended import create_access_token
from app import create_app
from app.helpers.extensions import db
from app.models import User, Task, Project


@pytest.fixture
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.test_client() as client:
        with app.app_context():
            db.create_all()

            # Create user 1
            user1 = User(id=1, email="user@gmail.com", username="User", password_hash="12345")
            db.session.add(user1)

            # Create user 2 (for test permission)
            user2 = User(id=2, email="user2@gmail.com", username="Other", password_hash="54321")
            db.session.add(user2)

            # Create project
            project = Project(id=1, name="Test Project", description="Test", created_by=1)
            db.session.add(project)

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

# ---------- Test cases ----------

def test_create_task(client, auth_headers_user1):
    res = client.post("/tasks/", json={
        "title": "Task from test",
        "description": "Testing task creation",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)

    assert res.status_code == 201
    assert res.json["message"] == "Task created"
    assert "id" in res.json
    print(res.json["id"])


def test_get_tasks(client, auth_headers_user1):
    # Create a task first
    client.post("/tasks/", json={
        "title": "Task from test",
        "description": "Testing",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)

    res = client.get("/tasks/", headers=auth_headers_user1)
    assert res.status_code == 200
    assert isinstance(res.json, list)
    assert len(res.json) >= 1


def test_update_task(client, auth_headers_user1):
    # Create task
    res = client.post("/tasks/", json={
        "title": "Temp",
        "description": "Test",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    # Update task
    res = client.put(f"/tasks/{task_id}", json={
        "title": "Updated Title",
        "description": "Updated desc"
    }, headers=auth_headers_user1)

    print(res)

    assert res.status_code == 200
    assert res.json["message"] == "Task updated"


def test_delete_task(client, auth_headers_user1):
    # Create task
    res = client.post("/tasks/", json={
        "title": "Delete Test",
        "description": "To be deleted",
        "assignee_id": 1,
        "project_id": 1
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    # Delete
    res = client.delete(f"/tasks/{task_id}", headers=auth_headers_user1)

    print(res)
    assert res.status_code == 200
    assert res.json["message"] == "Task deleted"


def test_forbidden_delete_other_users_task(client, auth_headers_user1, auth_headers_user2):
    
    res = client.post("/tasks/", json={
        "title": "Secret",
        "description": "Don't touch",
        "assignee_id": 1,
        "project_id": 1        
    }, headers=auth_headers_user1)
    task_id = res.json["id"]

    res = client.delete(f"/tasks/{task_id}", headers=auth_headers_user2)
    assert res.status_code == 403
    assert res.json["message"] == "Permission denied"

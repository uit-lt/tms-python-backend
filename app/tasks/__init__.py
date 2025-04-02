from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__)

# Import routes after blueprint creation to avoid circular imports
from app.tasks import routes
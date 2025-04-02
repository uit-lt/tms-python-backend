from flask import Blueprint

users_bp = Blueprint('tasks', __name__)

# Import routes after blueprint creation to avoid circular imports
from app.users import routes
from functools import wraps
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from flask import jsonify
from app.models import User, RolePermission, Permission, Role
from app.helpers.extensions import db

def has_permission(user_id, permission_name):
    """
    Check if the user has the given permission.
    """
    user = User.query.get(user_id)
    if not user:
        return False

    role_id = getattr(user, 'role_id', None)
    if not role_id:
        return False

    role_permissions = RolePermission.query.filter_by(role_id=role_id).all()
    permission_ids = [rp.permission_id for rp in role_permissions]

    permission = Permission.query.filter_by(name=permission_name).first()
    if not permission:
        return False

    return permission.id in permission_ids

def permission_required(permission_name):
    """
    Decorator to protect routes with a specific permission.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()

            if not has_permission(user_id, permission_name):
                return jsonify({"message": "Permission denied."}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator

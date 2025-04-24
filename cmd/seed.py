import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from faker import Faker
from app import create_app
from app.helpers.extensions import db
from app.models import User, Role, Permission, RolePermission
from werkzeug.security import generate_password_hash

fake = Faker()
app = create_app()

PASSWORD = "123456Aa@"


def user_exists(email, username):
    return User.query.filter((User.email == email) | (User.username == username)).first()


with app.app_context():
    print("Seeding users...")
    users = []

    for _ in range(10):
        while True:
            username = fake.user_name()
            email = fake.unique.email()
            if not user_exists(email, username):
                break

        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(PASSWORD)
        )
        users.append(user)

    db.session.add_all(users)
    db.session.commit()
    print("Seeded 10 fake users.")

    print("Seeding roles...")
    admin_role = Role(name="admin")
    member_role = Role(name="member")
    db.session.add_all([admin_role, member_role])
    db.session.commit()
    print("Roles created.")

    print("Seeding permissions...")
    perm_create = Permission(name="can_create_task", description="Can create task")
    perm_edit = Permission(name="can_edit_task", description="Can edit task")
    perm_delete = Permission(name="can_delete_task", description="Can delete task")
    db.session.add_all([perm_create, perm_edit, perm_delete])
    db.session.commit()
    print("Permissions created.")

    print("Mapping permissions to roles...")
    admin_perms = [
        RolePermission(role_id=admin_role.id, permission_id=perm.id)
        for perm in [perm_create, perm_edit, perm_delete]
    ]

    member_perms = [RolePermission(role_id=member_role.id, permission_id=perm_create.id)]

    db.session.add_all(admin_perms + member_perms)
    db.session.commit()
    print("Role-permission mappings done.")

    admin_user = users[0]
    admin_user.role_id = admin_role.id
    db.session.commit()
    print(f"Assigned admin role to user {admin_user.username}.")

    print("Seed complete.")

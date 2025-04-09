from app import create_app
from app.helpers.extensions import db
from werkzeug.security import generate_password_hash

from app.models import User

app = create_app()

with app.app_context():

    # Seed user
    user1 = User(
        username="admin",
        email="admin@example.com",
        password_hash=generate_password_hash("123456Aa@")
    )
    user2 = User(
        username="user",
        email="user@example.com",
        password_hash=generate_password_hash("123456Aa@")
    )
    db.session.add_all([user1, user2])
    db.session.commit()

    db.session.commit()

    print("✅ Seed data inserted!")

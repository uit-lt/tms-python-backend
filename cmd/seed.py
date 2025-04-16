from faker import Faker
from app import create_app
from app.helpers.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash

fake = Faker()
app = create_app()

PASSWORD = "123456Aa@"

def user_exists(email, username):
    return User.query.filter((User.email == email) | (User.username == username)).first()

with app.app_context():
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

    print("✅ Seeded 10 fake users successfully.")

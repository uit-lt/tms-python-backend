from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import app, db

from app.tasks.routes import task_bp
from app.users.routes import user_bp

migrate = Migrate()
ma = Marshmallow()


def create_app():

    migrate.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(user_bp, url_prefix="/users")

    return app

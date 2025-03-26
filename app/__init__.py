from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['HOST'] = config.FLASK_HOST
    app.config['PORT'] = config.FLASK_PORT

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.tasks.routes import task_bp
    from app.users.routes import user_bp

    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(user_bp, url_prefix="/users")

    return app

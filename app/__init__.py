from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from config import FLASK_HOST, FLASK_PORT

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.config['HOST'] = FLASK_HOST
    app.config['PORT'] = FLASK_PORT

    # echo some text to the console
    print("FLASK_HOST:", app.config['HOST'])

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from app.tasks.routes import tasks
    from app.users.routes import users

    app.register_blueprint(tasks, url_prefix="/tasks")
    app.register_blueprint(users, url_prefix="/users")

    return app

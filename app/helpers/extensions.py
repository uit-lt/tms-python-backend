from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# Create extensions instances
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
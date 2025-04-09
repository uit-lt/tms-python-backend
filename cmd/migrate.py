import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from flask import Flask
from flask_migrate import upgrade, migrate as flask_migrate, init as flask_init, stamp
from app.config import Config
from app.helpers.extensions import db, migrate
from app.models import User, Task

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        migrations_dir = Path("migrations")
        versions_dir = migrations_dir / "versions"

        if not migrations_dir.exists():
            print("🔧 Initializing migrations folder...")
            flask_init()
            versions_dir.mkdir(parents=True, exist_ok=True)
            stamp()  # đặt mốc version để tránh lỗi khi migrate
        elif not versions_dir.exists():
            versions_dir.mkdir(parents=True, exist_ok=True)

        print("📦 Generating migration script...")
        flask_migrate(message="initial")

        print("🚀 Applying migration...")
        upgrade()

        print("✅ Migration complete.")

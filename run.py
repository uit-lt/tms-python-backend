import os

from app import create_app

app = create_app()


@app.route("/")
def home():
    return "Hello world!"


if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST"),
        port=int(os.getenv("FLASK_PORT", "5000")),
        debug=os.getenv("DEBUG", "False"),
    )

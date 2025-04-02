import os

from app import create_app

app = create_app()

@app.route("/")
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(
        host=os.getenv("FLASK_HOST"),
        port=int(os.getenv("FLASK_PORT", "5000")),
        debug=os.getenv("DEBUG", "False"),
    )

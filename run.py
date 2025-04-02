import os

from app import create_app

app = create_app()

@app.route("/")
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG", False))

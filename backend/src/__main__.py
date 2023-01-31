"""This is an example file."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    """Main function."""
    return "Backend"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def greet():
    name = request.args.get("name", "Guest")
    return f"<h2>Hello, {escape(name)}!</h2>"

if __name__ == "__main__":
    app.run(debug=True)

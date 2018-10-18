from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def default():
    return "Hello world"


if __name__ == "__main__":
    app.run("localhost", 5001, debug=True)
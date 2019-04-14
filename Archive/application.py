#on Windows in Cs50AndWeb directory do:
# set  FLASK_APP=application.py
# then start application with:
#  $python -m run flask
# find result on localhost:5000

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world and Martin and Ute"

@app.route("/david")
def david():
    return "Hello,David!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Hello, {name}!</h1>"


if __name__ == "__main__":
    app.run()

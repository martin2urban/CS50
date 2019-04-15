#on Windows in Cs50AndWeb directory do:
# set FLASK_APP=app.py
#changes
#  set FLASK_DEBUG=1    ##allows auto reload
# then start application with:
#  $flask run
#  $python -m flask run
#  set FLASK_DEBUG=1    ##allows auto reload
# find result on localhost:5000
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods= ["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)

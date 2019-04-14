#on Windows in Cs50AndWeb directory do:
# set  FLASK_APP=application.py
#  set FLASK_DEBUG=1    ##allows auto reload
# then start application with:
#  $flask run
#  $python -m flask run
#  set FLASK_DEBUG=1    ##allows auto reload
# find result on localhost:5000

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    headline= "Hello, Martin world!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline= "Goodbye!"
    return render_template("index.html", headline=headline)




if __name__ == "__main__":
    app.run()

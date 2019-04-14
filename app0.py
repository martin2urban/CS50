#on Windows in Cs50AndWeb directory do:
# set  FLASK_APP=app.py
#  set FLASK_DEBUG=1    ##allows auto reload
# then start application with:
#  $flask run
#  $python -m flask run
#  set FLASK_DEBUG=1    ##allows auto reload
# find result on localhost:5000
import datetime
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    now=datetime.datetime.now()
    new_year=1 #now.month == 1 and now.day()
    return render_template("index.html", new_year=new_year)


if __name__ == "__main__":
    app.run()

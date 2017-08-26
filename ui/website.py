from flask import Flask, render_template, request
import json
import sqlite3
import sys
sys.path.append('/home/niko/Dev/Food/core')

from Dinner import Dinner

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/getDinner', methods=['GET'])
def getDinner():
    connection = sqlite3.connect("lite.db")
    dinner = Dinner(connection)
    item = dinner.getRandom()
    return json.dumps({'status': 'OK', 'data': {'item': item}})


@app.route('/addDinner', methods=['POST'])
def addDinner():
    connection = sqlite3.connect("lite.db")
    dinner = Dinner(connection)
    dinner.insert(request.form.get("newDinner"))
    return json.dumps({'status': 'OK', 'data': request.form.get("newDinner")})


if __name__ == "__main__":
    app.run(debug=True)

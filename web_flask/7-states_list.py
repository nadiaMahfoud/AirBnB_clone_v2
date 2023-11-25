#!/usr/bin/python3
""" A script that Starts a Flask web application """
from models import *
from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ it Returns an HTML page of all States sorted by name """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """ it Removes the current SQLAlchemy session. """
    storage.close()


if __name__ == "__main__":
    """ it Run on 0.0.0.0 """
    app.run(host='0.0.0.0')

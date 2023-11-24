#!/usr/bin/python3
"""A script that  Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ it Returns Hello HBNB! from 0.0.0.0:5000 """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ it Returns HBNB from 0.0.0.0:5000/hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0')

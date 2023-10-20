#!/usr/bin/python3
"""Defines a module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """The / triggers this function"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """The /hbnb triggers this function"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """The /c/... triggers this function"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/<text>', strict_slashes=False)
def hello_python(text="is cool"):
    """The python route triggers this function"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

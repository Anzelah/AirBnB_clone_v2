#!/usr/bin/python3
"""Defines a module"""
from models import storage
from flask import Flask, render_template



app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def view_states():
    """The route triggers this function"""
    all_states = storage.all("State")
    states = list()
    for state, value in all_states.items():
        states.append(value)

    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    """Remove current session after each request"""
    storage.close()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

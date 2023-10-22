#!/usr/bin/python3
"""Defines a module"""
from flask import Flask, render_template
#from models import storage
#from models.state import State
#from models.city import City


app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def view_states():
    """The route triggers this function"""
    all_states = storage.all(State)
    states = list()
    for state, value in all_states.items():
        states.append(value)

#    state_instance = State()
#    all_cities = state_instance.cities
    all_cities = storage.all(City)
    cities = list()

    for city, value in all_cities.items():
        cities.append(value)

    return render_template('8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def remove_session(exception):
    """Remove current session after each request"""
    storage.close()



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

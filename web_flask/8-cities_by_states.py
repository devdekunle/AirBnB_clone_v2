#!/usr/bin/python3
"""
a flask script that loads all cities and displays them in a url
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(exc):
    storage.close()


@app.route('/cities_by_states')
def cities_by_state():
    """ get all cities linked to a state"""

    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    all_cities = list(storage.all(City).values())
    all_cities.sort(key=lambda x: x.name)
    ctxt = {'states': all_states, 'cities': all_cities}
    return render_template('8-cities_by_states.html', **ctxt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=1)

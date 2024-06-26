#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage on teardown
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    Renders a HTML page with a list of all State objects
    """
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """
    Renders a HTML page with information about a specific State object
    """
    state = storage.get("State", id)
    if state is None:
        return render_template('9-states.html', state=None)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

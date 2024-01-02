#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states"""
from models import storage
from flask import Flask
from flask import render_template


app = Flast(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities
    sorted by cities"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exit):
    """close current alchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

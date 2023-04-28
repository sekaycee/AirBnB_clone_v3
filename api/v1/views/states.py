#!/usr/bin/python3
""" View for State objects that handles default API actions """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states():
    """ Retrieve the list of all State objects """
    return jsonify([obj.to_dict() for obj in storage.all(State).values()])

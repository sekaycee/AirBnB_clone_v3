#!/usr/bin/python3
""" Index view """
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ get http status as JSON """
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ get the number of each instance type as JSON """
    return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User"))

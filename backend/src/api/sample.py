from flask import Blueprint, request, g, jsonify

sample_api = Blueprint('sample_api', __name__)

@sample_api.route('/')
def sample():
    return "Sample API Ok", 200
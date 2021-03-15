from flask import Flask, g
from src.api.sample import sample_api

from src.config import MONGODB_URL
from src.models.db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': MONGODB_URL
}
initialize_db(app)

app.register_blueprint(sample_api, url_prefix='/sample')

@app.route("/")
def hello():
  return "Ok", 200

# Uncomment the following if you want to fix CORS header issues.
# @app.after_request
# def add_cors_headers(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', '*')
#   response.headers.add('Access-Control-Allow-Methods', "POST, PUT, GET, OPTIONS")
#   return response

#!/usr/bin/python3
"""
<<<<<<< HEAD
This module contains the principal application
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()


@app.errorhandler(404)
def page_not_foun(error):
    """ Loads a custom 404 page not found """
    return make_response(jsonify({"error": "Not found"}), 404)


app.config['SWAGGER'] = {
    'title': 'AirBnB clone - RESTful API',
    'description': 'This is the api that was created for the hbnb restful api project,\
    all the documentation will be shown below',
    'uiversion': 3}

Swagger(app)

if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)
=======
app
"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """
    teardown function
    """
    storage.close()

@app.errorhandler(404)
def handle_404(exception):
    """
    handles 404 error
    :return: returns 404 json
    """
    data = {
        "error": "Not found"
    }
    resp = jsonify(data)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
>>>>>>> 03aa4930f057d140fd8e80803821df7b6fe16c03

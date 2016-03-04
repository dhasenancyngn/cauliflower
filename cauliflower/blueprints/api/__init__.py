from flask import Blueprint

api = Blueprint('api', __name__)

import cauliflower.blueprints.api.v1
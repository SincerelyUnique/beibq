from flask import Blueprint

api = Blueprint("api", __name__)

import app.api.views

from flask import Blueprint

web = Blueprint("web", __name__)

import app.web.views

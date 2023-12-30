from flask import Blueprint

bp = Blueprint('metmuseum', __name__)


from app.metmuseum import routes

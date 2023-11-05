from flask import Blueprint

bp = Blueprint('jsonxmlcomparator', __name__)


from app.jsonxmlcomparator import routes
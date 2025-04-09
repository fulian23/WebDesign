from flask import Blueprint

search = Blueprint('search', __name__, url_prefix='/search')

@search.route('/')
def hello_world():
    return 'search'
from flask import Blueprint

from src.common.utils import response

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return response(True, 'Welcome', None)

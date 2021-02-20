from flask import Blueprint
from todos import todos_service

todos_controller_bp = Blueprint('todos_controller', __name__, url_prefix='/home', template_folder='../templates')


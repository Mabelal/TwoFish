from flask import render_template, Blueprint
from flask_login import login_required
from src.todos import todos_service

todos_controller_bp = Blueprint(
    "todos_controller", __name__, url_prefix="/home", template_folder="../templates"
)


@todos_controller_bp.route("/", methods=["GET"])
@login_required
def home():
    return render_template("home_form.html", title="Home")

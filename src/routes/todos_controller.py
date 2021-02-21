from flask import redirect, url_for, render_template, Blueprint
from flask_login import login_required
from src.todos import todos_service
from src.todos.todos_view import TodoForm

todos_controller_bp = Blueprint(
    "todos_controller", __name__, url_prefix="/home", template_folder="../templates"
)


@todos_controller_bp.route("/", methods=["GET", "POST"])
@login_required
def home():
    form = TodoForm()
    if form.validate_on_submit():
        todos_service.add_todo()
        # todos_service.delete_all()
        return redirect(url_for("todos_controller.home"))
    return render_template("home_form.html", title="Home", form=form, todos=todos_service.get_todos())

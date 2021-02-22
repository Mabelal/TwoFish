from flask import redirect, url_for, render_template, Blueprint
from flask_login import login_required
from src.todos import todos_service
from src.todos.todos_view import TodoForm

todos_controller_bp = Blueprint(
    "todos_controller", __name__, url_prefix="/home", template_folder="../templates"
)


@todos_controller_bp.route("/")
@login_required
def home():
    form = TodoForm()
    return render_template("home_form.html", title="Home", form=form, todos=todos_service.get_todos())


@todos_controller_bp.route("/add_todo", methods=["POST"])
def add_todo():
    todos_service.add_todo()
    return redirect(url_for("todos_controller.home"))


@todos_controller_bp.route("/delete_all", methods=["POST"])
def delete_all():
    todos_service.delete_all()
    return redirect(url_for("todos_controller.home"))


@todos_controller_bp.route("/mark_complete/<todo_id>", methods=["POST"])
def mark_complete(todo_id):
    todos_service.mark_complete(todo_id)
    return redirect(url_for("todos_controller.home"))


@todos_controller_bp.route("/edit/<todo_id>", methods=["POST"])
def edit(todo_id):
    # return redirect(url_for("todos_controller.home"))
    return 'todo' + todo_id + ' edit button pressed'


@todos_controller_bp.route("/delete/<todo_id>", methods=["POST"])
def delete(todo_id):
    todos_service.delete(todo_id)
    return redirect(url_for("todos_controller.home"))

from flask_login import current_user
from src.database.models import db, Todo


def get_todos():
    return current_user.todos.all()


def add_todo():
    todo = Todo(title="My first TODO", body="...", author=current_user)
    db.session.add(todo)
    db.session.commit()


def delete_all():
    todos = current_user.todos.all()
    for t in todos:
        db.session.delete(t)
    db.session.commit()

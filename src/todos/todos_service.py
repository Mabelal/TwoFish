from flask_login import current_user
from src.database.models import db, Todo
import datetime


def get_todos():
    return current_user.todos.all()


def add_todo():
    date = datetime.date.today()
    todo = Todo(body="My first TODO is to do this and that and that",
                is_complete=False,
                due_date=date,
                author=current_user)
    db.session.add(todo)
    db.session.commit()


def delete_all():
    todos = current_user.todos.all()
    for t in todos:
        db.session.delete(t)
    # if len(todos) > 0:
    #     db.session.delete(todos[-1])
    db.session.commit()


def mark_complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.is_complete = not todo.is_complete
    db.session.commit()


def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()

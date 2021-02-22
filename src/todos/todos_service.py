from flask_login import current_user
from src.database.models import db, Todo
import datetime


def get_todos():
    return current_user.todos.all()


def add_todo():
    todo = Todo(
        body="TODO",
        is_complete=False,
        is_editing=False,
        due_date=datetime.date.today(),
        author=current_user,
    )
    db.session.add(todo)
    db.session.commit()


def edit_todo(todo_id, body):
    todo = Todo.query.get(todo_id)

    if todo.is_editing:
        todo.body = body
    todo.is_editing = not todo.is_editing

    db.session.commit()


def mark_complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.is_complete = not todo.is_complete
    db.session.commit()


def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()


def set_date(todo_id, due_date):
    todo = Todo.query.get(todo_id)
    due_date = [int(x) for x in due_date.split('-')]
    todo.due_date = datetime.date(due_date[0], due_date[1], due_date[2])
    db.session.commit()

from flask_wtf import FlaskForm
from wtforms import BooleanField, DateTimeField, SubmitField


class TodoForm(FlaskForm):
    add_btn = SubmitField("Add TODO")
    delete_btn = SubmitField("Delete")
    is_complete = BooleanField()
    due_date = DateTimeField()

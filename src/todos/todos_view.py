from flask_wtf import FlaskForm
from wtforms import SubmitField


class TodoList(FlaskForm):
    add_btn = SubmitField("Add TODO")
    sort_btn = SubmitField("Order by due date")

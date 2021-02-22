from flask_wtf import FlaskForm
from wtforms import SubmitField


class TodoForm(FlaskForm):
    add_btn = SubmitField("Add TODO")
    sort_btn = SubmitField("Order by due date")

from flask_wtf import FlaskForm
from wtforms import SubmitField


class TodoForm(FlaskForm):
    add = SubmitField("Add TODO")
    delete = SubmitField("Delete")

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo
from src.database.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already in use.")

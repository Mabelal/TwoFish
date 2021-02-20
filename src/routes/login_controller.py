from flask import render_template, redirect, url_for, flash, Blueprint
from flask_login import current_user
from src.login.login_view import LoginForm
from src.login.registration_view import RegistrationForm
from src.login import login_service

login_controller_bp = Blueprint(
    "login_controller", __name__, url_prefix="/login", template_folder="../templates"
)


@login_controller_bp.route("/", methods=["GET", "POST"])
def login():
    # if current_user.is_authenticated:
    #     return "Already logged in brah"
    form = LoginForm()
    if form.validate_on_submit():
        user = login_service.login(
            form.username.data, form.password.data, form.remember_me.data
        )
        if user is not None:
            return "Hello world!"
        flash("Invalid username and/or password.")
    return render_template("login_form.html", title="Sign in", form=form)


@login_controller_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        login_service.register_user(form.username.data, form.password.data)
        flash("Your account has been created successfully.")
        return redirect(url_for("login_controller.login"))
    return render_template("registration_form.html", title="Register", form=form)

from flask import render_template, redirect, url_for, Blueprint
from login.login_form import LoginForm
from login.registration_form import RegistrationForm
from login import login_service

login_controller_bp = Blueprint("login_controller", __name__, url_prefix="/login", template_folder="../templates")


@login_controller_bp.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = login_service.get_user(form.username.data, form.password.data)
        if user is None:
            return 'nopeeeeee'
        return 'Hello world!'
    return render_template("login_form.html", title="Sign in", form=form)


@login_controller_bp.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        login_service.register_user(form.username.data, form.password.data)
        return redirect(url_for('login_controller.login'))
    return render_template('registration_form.html', title='Register', form=form)
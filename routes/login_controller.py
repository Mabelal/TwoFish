# from flask_login import LoginManager
# from forms import RegistrationForm
# login = LoginManager(app)
from flask import Blueprint

login_controller_bp = Blueprint("login_controller", __name__, url_prefix="/login", template_folder="../templates")


@login_controller_bp.route("/")
def login():
    # form = RegistrationForm()
    # return render_template('registration_form.html', title='Register', form=form)
    return 'login screen'

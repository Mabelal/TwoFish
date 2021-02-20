from flask_login import login_user, logout_user, LoginManager
from src.database.models import db, User

login_manager = LoginManager()
login_manager.login_view = "login_controller.login"


def login(username, password, remember):
    u = User.query.filter_by(username=username).first()
    if u is not None and u.check_password(password):
        login_user(u, remember)
        return u
    return None


def logout():
    logout_user()


def register_user(username, password):
    user = User(username, password)

    db.session.add(user)
    db.session.commit()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

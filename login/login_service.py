from flask_login import LoginManager
from database.models import db, User

login_manager = LoginManager()


def login(username, password, remember):
    u = User.query.filter_by(username=username).first()
    if u is not None and u.check_password(password):
        return u
    return None


def register_user(username, password):
    user = User(username, password)

    db.session.add(user)
    db.session.commit()

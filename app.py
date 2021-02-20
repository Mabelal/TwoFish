from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from config import Config
from routes.login_controller import login_controller_bp
from database.models import db
from login.login_service import login_manager

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login_controller_bp)

# Extensions
db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return redirect(url_for('login_controller.login'))


if __name__ == "__main__":
    app.run(port=8080)

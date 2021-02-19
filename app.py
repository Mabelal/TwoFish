from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.login_controller import login_controller_bp
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login_controller_bp)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# needed for database migrations and to prevent circular dependency
from database import models


@app.route("/")
def index():
    return redirect(url_for('login_controller.login'))


if __name__ == "__main__":
    app.run(port=8080)

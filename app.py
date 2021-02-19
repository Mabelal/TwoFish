from flask import Flask, redirect, url_for, render_template, request
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Flask
app = Flask(__name__)
app.config.from_object(Config)

# Database
db = SQLAlchemy(app)
from models import *

migrate = Migrate(app, db)


@app.route("/")
def index():
    # redirect to login_service
    return "MISTER CHU!!"


if __name__ == "__main__":
    app.run(port=8080)

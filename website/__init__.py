import os

from flask import Flask # pip install flask
from flask_sqlalchemy import SQLAlchemy # pip install flask-sqlalchemy
from os import path
from flask_login import LoginManager # pip install flask_login


def create_app():
    app = Flask(__name__)


    from .views import views

    app.register_blueprint(views, url_prefix="/")

    # http://localhost:5000  - use this to hit in browser

    return app


import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()  # SQL Alchemy instance
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'hello world'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # triple slash is a relative path
    db.init_app(app)



    from .views import views
    from .cookies import cookies

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(cookies, url_prefix="/")


    from .flaskDB import User, Post
    create_database(app)


    return app



def create_database(app):
    if not path.exists('website'+os.sep+DB_NAME):
        db.create_all(app=app)
        print('database created!')
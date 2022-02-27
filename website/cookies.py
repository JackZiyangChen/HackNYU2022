from flask import Blueprint, render_template, request, flash, make_response
from flask_login import login_required, current_user
from .flaskDB import Post, User
from . import db


cookies = Blueprint('cookies',__name__)

@cookies.route('/setcookie', methods=['POST', 'GET'])
def setcookie(): # setter
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('index.html'))
    resp.set_cookie('userID', user)

    return resp


@cookies.route('/getcookie')
def getcookie(): # getter
   name = request.cookies.get('userID')
   return '<h1>welcome ' + name + '</h1>'


from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .flaskDB import Post, User
from . import db
from sqlalchemy.sql import and_
from random import randint



views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        message = request.form.get('content')
        subject = request.form.get('title')
        if len(message) < 1:
            flash("message is too short", category="error")
        elif len(subject)<1:
            flash("please enter a subject", category="error")
        else:
            new_post = Post(content=message,subject=subject)

            # some code to check for user


            db.session.add(new_post)
            db.session.commit()
            print("data added")
            flash('Your message has been sent!', category='success')

    return render_template('index.html')


@views.route('/responses', methods=['GET','POST'])
def response_page():



    return render_template('responses.html')


def push_response(db, original, response):
    response.original_post = original.id

    db.session.add(response)
    db.session.commit()

    flash("Thank you for your response", category="success")



def pull_post():
    success = False
    while not success:
        id = randint(0, 999)
        post = Post.query.get(id)
        if post:
            if not post.is_pulled:
                post.is_pulled = True
                db.session.commit()
                return post




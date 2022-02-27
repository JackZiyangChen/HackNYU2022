from flask import Blueprint, render_template, request, flash, make_response, redirect, url_for
from flask_login import login_required, current_user
from .flaskDB import Post, User
from . import db
from sqlalchemy.sql import and_
from random import randint



views = Blueprint('views', __name__)


@views.route('/pull' )
def pull_message():
    post = pull_post()

    print(f'post: {post}')

    return redirect(url_for('views.home',post=post))



@views.route('/', methods=['GET','POST'])
def home():

    if not request.args.get('post'):
        post = ""
    else:
        post = request.args['post']

    if not ('user_id' in request.cookies):
        new_user = User()
        db.session.add(new_user)
        db.session.commit()
        user_id = new_user.id
        print(f'userid={user_id}')
        print(url_for('views.setcookie', user_id=user_id))
        return redirect(url_for('cookies.setcookie',user_id=user_id))

    else:
        user_id = request.cookies.get('user_id')
        print(f'cookie: {user_id}')




    if request.method == 'POST':
        message = request.form.get('content')
        subject = request.form.get('title')
        if len(message) < 1:
            flash("message is too short", category="error")
        elif len(subject)<1:
            flash("please enter a subject", category="error")
        else:
            new_post = Post(content=message,subject=subject,user_id=user_id)

            # some code to check for user


            db.session.add(new_post)
            db.session.commit()
            print("data added")
            flash('Your message has been sent!', category='success')

    return render_template('index.html',post=post)


@views.route('/responses', methods=['GET','POST'])
def response_page():
    u = User.query.filter_by(id=request.cookies.get("user_id")).first()

    if u:
        return render_template('responses.html',user=u)


def push_response(db, original, response):
    response.original_post = original.id

    db.session.add(response)
    db.session.commit()

    flash("Thank you for your response", category="success")



def pull_post():
    success = False
    tries = 0
    while not success:
        id = randint(0, 99)
        post = Post.query.filter_by(id=id).first()
        if post:
            if not post.is_pulled:
                post.is_pulled = True
                db.session.commit()
                success = True
                return post

        tries+=1
        if tries>10:
            success=True

    return post


def set_cookies(page, user):
    resp = make_response(render_template(page))
    resp.set_cookie('user_id', user)

    return resp




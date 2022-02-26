from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .flaskDB import Post, User
from . import db



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
            new_post = Post(content=message,title=subject)

            # some code to check for user


            db.session.add(new_post)
            db.session.commit()
            print("data added")
            flash('Your message has been sent!', category='success')

    return render_template('index.html')
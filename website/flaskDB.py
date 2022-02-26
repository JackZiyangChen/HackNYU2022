from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
from . import db

class Id(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User Id('{self.subject}', '{self.content}'"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(20), unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    content = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User Id('{self.subject}', '{self.date_posted}'"



letters = [
    {
        'subject': 'example 1',
        'content': 'content 1'

    },
    {
        'subject': 'example 2',
        'content': 'content 2'
    }


]
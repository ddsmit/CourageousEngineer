from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chrissmit import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    username = db.Column(db.String(20), unique=True, nullable=False, )
    email = db.Column(db.String(120), unique=True, nullable=False, )
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg', )
    password = db.Column(db.String(60), nullable=False, )
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f'User(username={self.username},email={self.email},image={self.image_file})'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    preview = db.Column(db.String(200), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True, default=None)
    content = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f'Post(title={self.username},preview={self.email},date={self.posted}'


from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chrissmit import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, )
    username = db.Column(db.String(20), unique=True, nullable=False, )
    full_name = db.Column(db.String(45), unique=False, nullable=False,)
    twitter_handle = db.Column(db.String(20), unique=True, nullable=False,)
    email = db.Column(db.String(120), unique=True, nullable=False, )
    image_file = db.Column(db.String(20), nullable=False, default='default.svg', )
    password = db.Column(db.String(60), nullable=False, )
    posts = db.relationship('Post', backref='author', lazy=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'User(id={self.id},username={self.username},email={self.email})'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aticle_id = db.Column(db.Integer, nullable=False,) #used for tracking ongoing changes
    is_ready_for_review = db.Column(db.Boolean, default=False,)
    is_released = db.Column(db.Boolean, default=False,)
    title = db.Column(db.String(100), nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    preview = db.Column(db.String(200), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True, default=None)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Post(title={self.username},preview={self.email},date={self.posted}'

class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True, default=None)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Post(title={self.username},preview={self.email},date={self.posted}'
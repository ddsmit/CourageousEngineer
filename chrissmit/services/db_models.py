from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from chrissmit import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, )
    authorization_level = db.Column(db.String(60), nullable=False, )
    linkedin = db.Column(db.String(100),)
    full_name = db.Column(db.String(45), unique=False, nullable=False,)
    twitter_handle = db.Column(db.String(20), unique=True, nullable=True,)
    email = db.Column(db.String(120), unique=True, nullable=False, )
    image_file = db.Column(db.String(20), nullable=False, default='default.svg', )
    password = db.Column(db.String(60), nullable=False, )
    articles = db.relationship('Article', backref='author', lazy=True)
    edits = db.relationship('ArticleEdits', backref='author', lazy=True)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'User(id={self.id},full_name={self.full_name},email={self.email})'

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_edit_id = db.Column(db.Integer, nullable=True) #Used to determine actual displayed content
    is_released = db.Column(db.Boolean, default=False,)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posted = db.Column(db.DateTime, nullable=True,)
    title = db.relationship('ArticleEdits', backref=backref('title', lazy=True)
    preview = db.relationship('ArticleEdits', backref='preview', lazy=True)
    content = db.relationship('ArticleEdits', backref='content', lazy=True)

    def __repr__(self):
        return f'Article(id={self.id},edit_id={self.edit_id},date={self.posted}'


class ArticleEdits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False,) #used for tracking ongoing changes
    is_edited = db.Column(db.Boolean, default=False,)
    is_ready_for_release = db.Column(db.Boolean, default=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    edited = db.Column(db.DateTime, nullable=True, default=datetime.utcnow) 
    title = db.Column(db.String(100), nullable=False,)
    preview = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(100), default='default.png')
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Article(title={self.title},preview={self.preview},date={self.edited}, edited={self.is_edited}, ready for release={self.is_ready_for_release}'


class Update(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited = db.Column(db.DateTime, nullable=True, default=None)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Post(title={self.title},posted={self.posted}'
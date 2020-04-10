from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Label
from wtforms.validators import DataRequired, Length, Email, EqualTo 

class UpdatesForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(),Length(min=2,max=20,),],
    )
    content = TextAreaField(
        'Content',
        validators=[DataRequired(),Length(min=2,max=255,),],
    )

    submit = SubmitField('Add Update')

class UpdateProfile(FlaskForm):
    full_name = StringField(
        'Full Name',
        validators=[DataRequired(), Length(min=2,max=50)],
    )
    user_name = StringField(
        'User Name',
        validators=[DataRequired(), Length(min=2,max=50)],
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), ]
    )
    twitter_handle = StringField(
        'Twitter Handle',
        validators=[DataRequired(),]
    )
    image_file = StringField(
        'Image File Name',
        validators=[DataRequired(),],
    )
    content = TextAreaField(
        'About/Bio',
        validators = [DataRequired()]
    )
    submit = SubmitField('Update Profile')

    # id = db.Column(db.Integer, primary_key=True, )
    # username = db.Column(db.String(20), unique=True, nullable=False, )
    # full_name = db.Column(db.String(45), unique=False, nullable=False,)
    # twitter_handle = db.Column(db.String(20), unique=True, nullable=False,)
    # email = db.Column(db.String(120), unique=True, nullable=False, )
    # image_file = db.Column(db.String(20), nullable=False, default='default.svg', )
    # password = db.Column(db.String(60), nullable=False, )
    # posts = db.relationship('Post', backref='author', lazy=True)
    # content = db.Column(db.Text, nullable=False)
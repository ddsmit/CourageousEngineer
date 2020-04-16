from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from chrissmit.services import profile
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Label
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError 

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
    linkedin = StringField(
        'LinkedIn',
        validators=[DataRequired(), Length(min=2,max=100)],
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), ]
    )
    twitter_handle = StringField(
        'Twitter Handle',
        validators=[DataRequired(),]
    )
    image_file = FileField(
        'Choose New Profile Image',
        validators=[FileAllowed(['svg','png','jpg']),],
    )
    content = TextAreaField(
        'About/Bio',
        validators = [DataRequired()]
    )
    submit = SubmitField('Update Profile')

    def validate_email(self, email):
        if email.data != current_user.email:
            if profile.get(email.data):
                raise ValidationError("That email is already used.")

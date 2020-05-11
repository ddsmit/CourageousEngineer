from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from chrissmit.services import profile, messages
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, Label, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL 

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
        validators=[DataRequired(), Length(min=2,max=100), URL()],
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


class ArticleForm(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(), Length(min=2,max=100)],
    )
    preview = StringField(
        'Article Preview',
        validators=[DataRequired(), Length(min=2,max=200)],
    )
    content = TextAreaField(
        'Article',
        validators = [DataRequired()]
    )
    image_file = FileField(
        'Choose Image for Article',
        validators=[FileAllowed(['svg','png','jpg']),],
    )
    tags = SelectMultipleField(
        'Tags',
        choices=[],
    )
    save = SubmitField('Save')
    step_forward = SubmitField('Step Forward')
    step_backward = SubmitField('Send Back')

class ContactForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(min=2,max=100)],
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(),],
    )
    reason = SelectField(
        'Why are you contacting us?',
        # validate_choice=False,
        choices=[],
    )
    content = TextAreaField(
        'Article',
        validators = [DataRequired()]
    )
    submit = SubmitField('Send')

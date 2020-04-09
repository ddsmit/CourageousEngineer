from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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

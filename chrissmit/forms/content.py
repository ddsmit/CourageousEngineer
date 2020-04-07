from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UpdatesFrom(FlaskForm):
    title = StringField(
        'Title',
        validators=[DataRequired(),Length(min=2,max=20,),],
    )
    content = StringField(
        'Content',
        validators=[DataRequired(),Length(min=2,max=255,),],
    )

    submit = SubmitField('Add Update')

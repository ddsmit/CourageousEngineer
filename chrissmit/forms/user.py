from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from chrissmit.services.db_models import User

class RegistrationFrom(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(),Length(min=2,max=20,),],
    )
    email = StringField(
        'Email',
        validators=[DataRequired(),Email(),]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(),Length(min=8),],
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(),Length(min=8),EqualTo('password'),],
    )

    submit = SubmitField('Sign Up')


class LogInForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email(), ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=8), ],
    )
    remember = BooleanField(
        'Remember Me',
    )
    submit = SubmitField('Log In')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("Not a valid user's email")
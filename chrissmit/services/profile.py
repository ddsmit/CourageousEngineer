from chrissmit.services.db_models import User
from chrissmit import bcrypt, db
from flask_login import current_user

def get_all():
    return User.query.all()


def get(email):
    return User.query.filter_by(email=email).first()

def is_password_correct(user_password, entered_password):
    return bcrypt.check_password_hash(user_password, entered_password)

def update(form):
    current_user.full_name=form.full_name.data
    current_user.username=form.user_name.data
    current_user.email=form.email.data
    current_user.twitter_handle=form.twitter_handle.data
    current_user.image_file=form.image_file.data
    current_user.content=form.content.data
    db.session.commit()

def update_form_data(form):
    form.full_name.data = current_user.full_name
    form.user_name.data = current_user.username
    form.email.data = current_user.email
    form.twitter_handle.data = current_user.twitter_handle
    form.image_file.data = current_user.image_file
    form.content.data = current_user.content
    return form


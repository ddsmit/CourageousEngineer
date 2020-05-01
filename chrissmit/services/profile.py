from chrissmit.services.db_models import User
from chrissmit import bcrypt, db, app
from flask_login import current_user


def get_all():
    return User.query.all()

def all_access():
    return bcrypt.check_password_hash(current_user.authorization_level, 'all_access')


def get(email=None,id=None):
    if email:
        return User.query.filter_by(email=email).first()
    elif id:
        return User.query.filter_by(id=id).first()

def is_password_correct(user_password, entered_password):
    return bcrypt.check_password_hash(user_password, entered_password)

def update(form):
    current_user.full_name=form.full_name.data
    current_user.linkedin=form.linkedin.data
    current_user.email=form.email.data
    current_user.twitter_handle=form.twitter_handle.data
    current_user.content=form.content.data
    db.session.commit()

def update_form_data(form):
    form.full_name.data = current_user.full_name
    form.linkedin.data = current_user.linkedin
    form.email.data = current_user.email
    form.twitter_handle.data = current_user.twitter_handle
    form.image_file.data = current_user.image_file
    form.content.data = current_user.content
    return form
from chrissmit.services.db_models import User
from chrissmit import bcrypt, db, app, mail
from flask_login import current_user
from flask import url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Message


def get_all():
    return User.query.all()

def all_access():
    return bcrypt.check_password_hash(current_user.authorization_level, 'all_access')


def get(email=None,id=None):
    if email:
        return User.query.filter_by(email=email).first()
    elif id:
        return User.query.filter_by(id=int(id)).first()

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

def get_reset_token(user_id, expires_seconds=15*60):
    serializer = Serializer(app.config['SECRET_KEY'], expires_seconds)
    return serializer.dumps({'user_id':user_id}).decode('utf-8') 

def verify_reset_token(token):
    serializer = Serializer(app.config['SECRET_KEY'])
    try:
        user_id = serializer.loads(token)['user_id']
    except:
        return None
    return get(id=user_id)

def update_reset_form(user, form):
    form.email.data = user.email
    return form

def update_password(user, form):
    hashed_password = bcrypt.generate_password_hash(form.confirm_password.data)
    user.password=hashed_password
    db.session.commit()

def update_password_email(user):
    token = get_reset_token(user.id)
    message = Message(
        'Password Change Request', 
        sender='david.smit@courageousengineer.com', 
        recipients=[user.email],
    )
    message.body = f"""
Hello {user.full_name},
To reset your password, visit the following link:
{url_for('user.reset_password', token=token, _external=True)}
If you did not make this request, please let us know and we will investigate.
Thanks,
David Smit
    """
    mail.send(message)


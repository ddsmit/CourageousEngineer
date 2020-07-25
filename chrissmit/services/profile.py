from chrissmit.services.db_models import User
from chrissmit import bcrypt, db, app
from flask_login import current_user
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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

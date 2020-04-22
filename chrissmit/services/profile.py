from chrissmit.services.db_models import User
from chrissmit import bcrypt, db, app
from flask_login import current_user
import secrets
import pathlib
from PIL import Image

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

def delete_current_picture():
    picture_path = pathlib.Path(
                app.root_path, 
                'static', 
                'img', 
                'authors',
                current_user.image_file,
            )
    if picture_path.exists():
        picture_path.unlink()
        

def save_picture(image_file):
    if image_file:
        image_hex = secrets.token_hex(8)
        image_path = pathlib.Path(image_file.filename)
        file_extension = image_path.suffix
        new_file_path = pathlib.Path(
            app.root_path, 
            'static', 
            'img', 
            'authors',
            image_hex + file_extension,
        )
        if file_extension != '.svg':
            output_size = (500,500)
            image_file = Image.open(image_file)
            image_file.thumbnail(output_size)
        image_file.save(str(new_file_path))            
        file_name = new_file_path.name
    else:
        file_name = current_user.image_file
    
    current_user.image_file = file_name
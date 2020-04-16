from chrissmit.services.db_models import User
from chrissmit import bcrypt, db, app
from flask_login import current_user
import secrets
import pathlib
from PIL import Image

def get_all():
    return User.query.all()


def get(email):
    return User.query.filter_by(email=email).first()

def is_password_correct(user_password, entered_password):
    return bcrypt.check_password_hash(user_password, entered_password)

def update(form, picture_filename):
    current_user.full_name=form.full_name.data
    current_user.linkedin=form.linkedin.data
    current_user.email=form.email.data
    current_user.twitter_handle=form.twitter_handle.data
    current_user.image_file=picture_filename
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
        print(file_extension)
        if file_extension != '.svg':
            output_size = (500,500)
            image_file = Image.open(image_file)
            image_file.thumbnail(output_size)
        image_file.save(str(new_file_path))            
        file_name = new_file_path.name
    else:
        file_name = current_user.image_file
    print(file_name)
    return file_name
from chrissmit import app
import secrets
import pathlib
from PIL import Image

def create_filepath(filename, subdirectory):
    return pathlib.Path(
        app.root_path, 
        'static', 
        'img', 
        subdirectory,
        filename,
    )

def delete(filename, subdirectory):
    picture_path = create_filepath(filename, subdirectory)
    if picture_path.exists():
        picture_path.unlink()
        

def save(image_file, subdirectory, desired_width=800):
    if image_file:
        image_hex = secrets.token_hex(8)
        image_path = pathlib.Path(image_file.filename)
        file_extension = image_path.suffix
        new_file_path = create_filepath(image_hex + file_extension, subdirectory)
        if file_extension != '.svg':
            image_file = Image.open(image_file)
            if image_file.width > desired_width:
                resize_factor = image_file.width/desired_width
            else:
                resize_factor = 1
            image_file.thumbnail((image_file.width,500))
            image_file.reduce(int(resize_factor))
        image_file.save(str(new_file_path))            
        file_name = new_file_path.name
        return file_name

def save_preview(image_file, file_name):
    if image_file:
        image_path = pathlib.Path(image_file.filename)
        file_extension = image_path.suffix
        if file_extension != '.svg':
            output_size = (1200,628)
            image_file = Image.open(image_file)
            image_file.thumbnail(output_size)
            new_file_path = create_filepath(file_name, 'preview')
            image_file.save(str(new_file_path))

def get_preview(image_file):
    if  not ('.svg' in image_file or '.ico' in image_file):
        return 'https://www.courageousengineer.com/static/img/preview/' + image_file
        
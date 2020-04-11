from chrissmit import db, bcrypt
from chrissmit.services.db_models import User, Post, Update

db.drop_all()
db.create_all()

yolanda = User(
    username='chrissmit',
    full_name='Yolanda Smit',
    twitter_handle='@yoyosmit',
    email='yolanda.smit@courageousengineer.com',
    image_file = 'yoyo.svg',
    password = bcrypt.generate_password_hash('M!$$y0y0'),
    content = 'She is awesome',
)

david = User(
    username='ddsmit',
    full_name='David Smit',
    twitter_handle='@davidouglasmit',
    email='david.smit@courageousengineer.com',
    image_file = 'yoyo.svg',
    password = bcrypt.generate_password_hash('P@$$w0rd%12'),
    content = 'He is awesome',
)

db.session.add(yolanda)
db.session.add(david)
db.session.commit()
import os
import json
import pathlib

config_path = pathlib.Path('etc/config.json')

with open(config_path) as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
    RECAPTCHA_PUBLIC_KEY = config.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = config.get('RECAPTCHA_PRIVATE_KEY')
    MAIL_SERVER = config.get('MAIL_SERVER')
    MAIL_PORT = config.get('MAIL_PORT') 
    MAIL_USE_TLS = config.get('MAIL_USE_TLS')
    MAIL_USE_SSL = config.get('MAIL_USE_SSL')
    MAIL_USERNAME = config.get('MAIL_USERNAME')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD')



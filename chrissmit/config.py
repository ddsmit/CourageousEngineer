import os
import json
import pathlib

config_path = pathlib.Path('etc/config.json')

with open(config_path) as config_file:
    config = json.load(config_file)

class Config:
    SECRET_KEY = config.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')

import flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from chrissmit.views import blueprints


app = flask.Flask(__name__)
blueprints.register(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY']='c41af915fbe41ebd20e4b772ef88d4a6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
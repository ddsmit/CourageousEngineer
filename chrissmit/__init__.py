import flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from chrissmit.views import blueprints


app = flask.Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
blueprints.register(app)


app.config['SECRET_KEY']='c41af915fbe41ebd20e4b772ef88d4a6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from chrissmit.views import blueprints


app = flask.Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
blueprints.register(app)


app.config['SECRET_KEY']='c41af915fbe41ebd20e4b772ef88d4a6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
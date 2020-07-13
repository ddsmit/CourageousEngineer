import flask
from chrissmit.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from chrissmit.views import blueprints
from secure import SecureHeaders

secure_headers = SecureHeaders()

app = flask.Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
blueprints.register(app)

app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['RECAPTCHA_PUBLIC_KEY'] = Config.RECAPTCHA_PUBLIC_KEY
app.config['RECAPTCHA_PRIVATE_KEY'] = Config.RECAPTCHA_PRIVATE_KEY

@app.after_request
def set_secure_headers(response):
    secure_headers.flask(response)
    return response
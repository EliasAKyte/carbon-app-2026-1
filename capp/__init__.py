from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)

application.config['SECRET_KEY'] = os.environ['SECRET_KEY']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)

login_manager = LoginManager(application)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

from capp.models import User, Transport
from capp.home.routes import home
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

with application.app_context():
    db.create_all()

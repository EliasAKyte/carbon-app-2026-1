from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

application = Flask(__name__)

application.config['SECRET_KEY'] = os.environ['SECRET_KEY']  
DBVAR = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}/{os.environ['RDS_DB_NAME']}"
DBVAR = 'postgresql://postgres:Elias2508@awseb-e-c4u3cmzhpu-stack-awsebrdsdatabase-izxex7zvyex6.cv2qy82mqgnx.eu-north-1.rds.amazonaws.com:5432/ebdb'

application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
application.config['SQLALCHEMY_BINDS'] = {'transport': DBVAR}

# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# application.config['SQLALCHEMY_BINDS']={'transport': 'sqlite:///transport.db'}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager=LoginManager(application)
login_manager.login_view="users.login"
login_manager.login_message_category="info"

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

with application.app_context():
    db.create_all()




from capp import application, db
from capp.models import *

with application.app_context():
    db.create_all()
    print("Tables created!")

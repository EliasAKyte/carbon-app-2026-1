from capp import application, db

with application.app_context():
    db.create_all()
    print("Tables created!")

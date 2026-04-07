from capp import application
from flask_sqlalchemy import SQLAlchemy
import os

application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///user.db')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

class User(db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    transport = db.relationship('Transport', backref='author', lazy=True)

class Transport(db.Model):
    __tablename__='transport_table'
    id = db.Column(db.Integer, primary_key=True)
    kms = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)

if __name__ == '__main__':
    application.run(debug=True)

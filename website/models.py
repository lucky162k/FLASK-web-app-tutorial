# Here is where the database models will be created.
# From the means the current directory that is website where such is located in __init__.py
from . import db
# Flask login - UserMixin supports logging of users
from flask_login import UserMixin
# The func will be able to record the now timestamp
from sqlalchemy.sql import func

# Schema setup for the database

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


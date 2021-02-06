from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# database models
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_assoc = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    # creating an ID for every user
    id = db.Column(db.Integer, primary_key=True)
    # store the email
    # of the user String(150) = max. 150 letters in an
    # email and make it unique
    email = db.Column(db.String(150), unique=True)
    # store the password and the first name, max 150 chars
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # make a relationship between the user and the notes
    # database
    notes = db.relationship('Note')

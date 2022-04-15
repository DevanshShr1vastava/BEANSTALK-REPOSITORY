from __future__ import unicode_literals
from sqlalchemy import PrimaryKeyConstraint
from . import db
#importing from the current package "Website" using . "db"
from flask_login import UserMixin
#UserMixin is a Custom class
from sqlalchemy.sql import func

class Note(db.Model):#inheriting Model class which is in db class
    #general notes data table
    id = db.Column(db.Integer, primary_key = True) 
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True),default = func.now())
    #func.now gets the current date 
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #creating a foreign key to establish relationship between the objects/tables    
    #foreign key for one to many relationship
    #so say for one user we have many notes

class User(db.Model, UserMixin):
    #user data table
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    #whenever that user enters data store in notes with the established relationship



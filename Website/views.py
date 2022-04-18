#this is where we tell what page to go to and stuff
from unicodedata import category
from flask import Blueprint, jsonify,render_template,request,flash
from flask_login import login_required, current_user
from .models import Note
import json
import sqlite3
from . import db
#this file is a blueprint of our application
#this has a bunch of URLs to find
views  = Blueprint('views',__name__)
#we have now setup a blueprint for our flask application

@views.route('/',methods = ["GET","POST"])
@login_required #we cannot get to the home page unless the user is logged in 
#this function will run whenever we go to / 
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!' ,category ='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})


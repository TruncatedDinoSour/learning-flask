import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('note is too short!', category='error')
        elif len(note) > 9999:
            flash('note is too big!', category='error')
        else:
            new_note = Note(data=note, user_assoc=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Created', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    note_id = note['noteID']
    note = Note.query.get(note_id)
    if note:
        if note.user_assoc == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note Deleted', category='success')
        else:
            flash('note could not be deleted as you don\'t own it', category='error')
    else:
        flash('note could not be found', category='error')
    return jsonify({})

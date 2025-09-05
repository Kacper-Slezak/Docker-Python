from app import app, db
from app.models import Note
from flask import render_template, request, redirect, url_for
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        note_content = request.form.get('note_content')
        if note_content:
            new_note = Note(content=note_content)
            db.session.add(new_note)
            db.session.commit()
    
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@app.route('/delete_note/<int:note_id>')
def delete_note(note_id):
    note_to_delete = Note.query.get_or_404(note_id)
    db.session.delete(note_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

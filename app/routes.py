# Autor: Claudia Leins
# Erstellungsdatum: 2025-07-09
# Beschreibung: 
# API-Routen für den SmartTaskBot.
# Enthält alle REST-Endpoints für Aufgabenverwaltung:
# - Anzeigen, Hinzufügen, Aktualisieren und Löschen von Tasks
# - Validierung von Eingabedaten
# - JSON-basierte Kommunikation
#-----------------------------------------------------------------

from flask import Blueprint, request, jsonify
from .models import db, Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "SmartTaskBot API läuft!"})

# Alle Aufgaben anzeigen
@main.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Neue Aufgabe hinzufügen
@main.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Titel erforderlich"}), 400
    
    try:
        due = datetime.strptime(data['due_date'], "%Y-%m-%d").date() if 'due_date' in data else None
    except ValueError:
        return jsonify({"error": "Falsches Datumsformat. Erlaubt: YYYY-MM-DD"}), 400


    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=due,
        priority=int(data.get('priority', 2))
    )
    
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# Aufgabe aktualisieren (z. B. als erledigt markieren)
@main.route('/api/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if 'done' in data:
        task.done = data['done']
        db.session.commit()
        return jsonify(task.to_dict())
    else:
        return jsonify({"error": "Kein gültiger Parameter"}), 400

# Aufgabe löschen
@main.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Aufgabe gelöscht"})
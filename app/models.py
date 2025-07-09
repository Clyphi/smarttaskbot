# Autor: Claudia Leins
# Erstellungsdatum: 2025-07-09
# Beschreibung: 
# Datenbankmodelle für die SmartTaskBot Anwendung.
# Definiert das Task-Modell mit Feldern für Titel, Beschreibung,
# Fälligkeitsdatum, Priorität und Erledigungsstatus.
#-----------------------------------------------------------------

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.Integer, default=2)  # 1=hoch, 2=mittel, 3=niedrig
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "priority": self.priority,
            "done": self.done
        }

    def __repr__(self):
        return f"<Task {self.id}: {self.title} - {'Erledigt' if self.done else 'Offen'}>"
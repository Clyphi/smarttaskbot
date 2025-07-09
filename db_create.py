# Autor: Claudia Leins
# Erstellungsdatum: 2025-07-09
# Beschreibung: 
# Initialisiert die Flask-Anwendung und erstellt alle Datenbanktabellen.
# Verwendung:
# - Wird beim ersten Setup ausgeführt, um die Datenbankstruktur zu erstellen.
# - Nutzt SQLAlchemy für die Tabellenerstellung basierend auf den Models.
#-----------------------------------------------------------------

from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Datenbank wurde erstellt.")
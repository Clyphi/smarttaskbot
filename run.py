# Autor: Claudia Leins
# Erstellungsdatum: 2025-07-09
# Beschreibung: 
# Initialisiert die Flask-Anwendung und erstellt die Datenbankstruktur.
# Erzeugt alle definierten Datenbanktabellen via SQLAlchemy und gibt
# eine Übersicht der vorhandenen Tabellen aus. Startet den Flask-Dev-Server
# im Debug-Modus bei direkter Ausführung.
#-----------------------------------------------------------------

from app import create_app
from app.models import db


app = create_app()

# Diese Zeile erzeugt die Datenbankdatei und Tabellen
with app.app_context():
    print(">>> Starte Datenbank-Erstellung")
    db.create_all()
    # Tabellen ausgeben
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    print(">>> Tabellen gefunden:", tables)
    print(">>> Datenbank erstellt (sofern nötig)")
if __name__ == '__main__':
    app.run(debug=True)
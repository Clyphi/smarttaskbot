# SmartTaskBot 🚀

![SmartTaskBot Logo](/images/logo.png)  
*Intelligenter Aufgabenmanager mit grafischer Oberfläche*


## 🛠️ Installation & Einrichtung

### Voraussetzungen
- Python 3.8 oder höher
- pip (wird normalerweise mit Python installiert)
- SQLite (in Python enthalten)


### 1. Projekt klonen und einrichten

```bash
# 1. Repository klonen
git clone https://github.com/Clyphi/smarttaskbot.git

# 2. Ins Projektverzeichnis wechseln
cd SmartTaskBot

# 3. Virtuelle Umgebung erstellen (empfohlen)
python -m venv venv

# 4. Umgebung aktivieren
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# 5. Abhängigkeiten installieren
pip install -r requirements.txt

# 6. Datenbank initialisieren
python db_create.py

### 2. Backend starten

```bash
python run.py

Hinweis: Lassen Sie dieses Terminal geöffnet - der Server muss laufen!

### 3. Oberfläche starten

```bash
python gui_client.py


✨ Hauptfunktionen

Aufgabenverwaltung
✅ Neue Aufgaben hinzufügen
✏️ Aufgaben bearbeiten
🗑️ Aufgaben löschen
✔️ Als erledigt markieren
Benutzerfreundliche Oberfläche
🖱️ Einfache Bedienung per Maus
🔄 Automatische Aktualisierung
🎨 Klare visuelle Statusanzeige


⚙️ Technische Architektur

Backend
Flask (Python Web Framework)
SQLAlchemy (Datenbank ORM)
RESTful API
Frontend
Tkinter (GUI Toolkit)
Thread-basierte Aktualisierung


📂 Projektstruktur

```text
smarttaskbot/
├── app/               # Backend-Code (Flask)
│   ├── __init__.py
│   └── models.py      # Datenbankmodelle
├── migrations/        # Datenbank-Migrationen
├── images/            # Bildassets
│   └── logo.png
├── gui_client.py      # Haupt-GUI
├── run.py             # Backend-Starter
├── requirements.txt   # Abhängigkeiten
└── README.md          # Diese Datei


❓ Hilfe & Support

Probleme melden:
GitHub Issues
Feature Requests:
Per Issue mit dem Label "enhancement"


📜 Lizenz

MIT License
© 2023 [Claudia Leins] - Siehe LICENSE Datei
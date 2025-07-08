from flask import Flask
from .models import db
from .routes import main
import os




def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir,'..', 'smarttaskbot.db') # eine Ebene über app/('instance')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smarttaskbot.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main)

    return app
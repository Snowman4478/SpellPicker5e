from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # Load config settings
    app.config.from_object('config.Config')

    db.init_app(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    with app.app_context():
        from . import routes, models
    

    with app.app_context():
        db.create_all()
    

    return app

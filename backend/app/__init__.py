from flask import Flask
from flask_cors import CORS

def create_app():

    app = Flask(__name__)

    # Load config settings
    app.config.from_object('config.Config')

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

    with app.app_context():
        from . import routes
    

    return app

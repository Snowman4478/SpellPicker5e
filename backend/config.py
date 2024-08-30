import os
from dotenv import load_dotenv

#Load environment variables from .env file
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =  f'sqlite:///{os.path.join(basedir, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_AUTO_RELOAD = True


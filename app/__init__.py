from flask import Flask
from app.models import db
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.init_app(app)
    from app.controllers.main import main
    app.register_blueprint(main)
    return app
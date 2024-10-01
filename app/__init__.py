from flask import Flask
from app.models import db
from app.controllers import farmer_bp
from app.controllers import bank
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['TRACK_MODIFICATIONS'] = os.getenv('TRACK_MODIFICATIONS')
    db.init_app(app)
    from app.controllers.dairy_owner_controller import dairy
    app.register_blueprint(bank)
    app.register_blueprint(dairy)
    app.register_blueprint(farmer_bp)
    return app
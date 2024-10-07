from flask import Flask
from app.models import db
from app.controllers import farmer_bp, bank, dairy, muster_, supplies, supply_transaction
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['TRACK_MODIFICATIONS'] = os.getenv('TRACK_MODIFICATIONS')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    db.init_app(app)
    app.register_blueprint(muster_)
    app.register_blueprint(supply_transaction)
    print(app.template_folder)
    app.register_blueprint(supplies)
    app.register_blueprint(bank)
    app.register_blueprint(dairy)
    app.register_blueprint(farmer_bp)
    return app
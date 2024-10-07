from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.farmer import farmers
from app.models.cow import cows
from app.models.dairyowner import dairy_owner
from app.models.farmer_bank import farmer_bank_details
from app.models.muster_data import muster
from app.models.supplies import Supplies
from app.models.supply_transaction import SupplyTransaction

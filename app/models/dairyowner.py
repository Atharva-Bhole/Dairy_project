from . import db
from flask import current_app as app
from .farmer import farmers
from .supplies import Supplies
from .transactions import Transaction
from .muster_data import muster

class dairy_owner(db.Model):
    __tablename__ = 'dairy_owner'

    # A unique dairy id given to each dairy owner Auto Incremental starting from 1
    dairy_id = db.Column(db.Integer(), primary_key = True)

    # Dairy Name - Varchar
    dairy_name = db.Column(db.String())

    # State of the dairy - Varchar
    state = db.Column(db.String())

    # Taluka of the dairy - Varchar
    taluka = db.Column(db.String())

    # District of the dairy - Varchar
    district = db.Column(db.String())

    # Village of the dairy - Varchar
    village = db.Column(db.String())

    # Data of dairy owner created at - Date
    created_at = db.Column(db.Date)

    # Most recent date when dairy data was updated - Date
    updated_at = db.Column(db.Date)

    # Date of deletion of dairy owner - Date   null if not deleted
    deleted_at = db.Column(db.Date)

    # Foreign key relation mapping in farmers table
    farmers = db.relationship('farmers', backref='dairy_owner', lazy=True)

    # Foreign Key relation mapping in supply table
    supply = db.relationship('Supplies', backref='dairy_owner', lazy=True)

    # Foreign key relation mapping in transaction table
    transactions = db.relationship('Transaction', backref='dairy_owner', lazy=True)

    
    # Commented out because unsure to add dairy_id in muster data or not 
    # Also dairy_id is commented out from muster_data model
    
    # muster = db.relationship('muster', backref='dairy_owner', lazy=True)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    def __repr__(self):
        return f"Dairy Name {self.dairy_name}, Dairy Id {self.dairy_id}"

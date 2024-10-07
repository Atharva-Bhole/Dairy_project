from . import db
from flask import current_app as app 
# Do not remove these redundant classes they are showing as redundant but used in db.relationship()
from .muster_data import muster
from .cow import cows
from .farmer_bank import farmer_bank_details
from .muster_data import muster
from .cow import cows
from .farmer_bank import farmer_bank_details
from .transactions import Transaction
from .supply_transaction import SupplyTransaction

class farmers(db.Model):
    __tablename__ = 'farmers'
    farmer_id = db.Column(db.Integer, primary_key=True)
    dairy_id = db.Column(db.Integer, db.ForeignKey('dairy_owner.dairy_id'))
    state = db.Column(db.String())
    name = db.Column(db.String())
    contact_number = db.Column(db.String(length=15))
    address = db.Column(db.String())
    taluka = db.Column(db.String())
    district = db.Column(db.String())
    village = db.Column(db.String())
    wallet_balance = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    deleted_at = db.Column(db.Date)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    
    cow = db.relationship('cows', backref='farmers', lazy=True)
    # muster = db.relationship('muster', backref='farmers', lazy=True)
    muster_by_name = db.relationship('muster', backref='farmers_by_name', lazy=True, foreign_keys='muster.farmer_name')
    muster_by_id = db.relationship('muster', backref='farmers_by_id', lazy=True, foreign_keys='muster.farmer_id')
    farmer_bank = db.relationship('farmer_bank_details', backref='farmers', lazy=True)
    supply_transaction = db.relationship('SupplyTransaction', backref='farmers', lazy=True)
    transactions = db.relationship('Transaction', backref='farmers', lazy=True)
    def __repr__(self):
        return f"Farmer Name {self.name}, FarmerID {self.farmer_id}"
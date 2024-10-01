from . import db
from flask import current_app as app 

class farmers(db.Model):
    __tablename__ = 'farmers'
    farmer_id = db.Column(db.Integer, primary_key=True)
    dairy_id = db.Column(db.Integer, db.ForeignKey('dairyowner.dairy_id'))
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

    def __repr__(self):
        return f"Farmer Name {self.name}, FarmerID {self.farmer_id}"
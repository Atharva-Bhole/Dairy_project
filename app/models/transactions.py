from . import db
from flask import current_app as app 

class Transaction(db.Model):
    __tablename__ = 'transactions'

    transaction_id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.farmer_id'), nullable=False)
    dairy_id = db.Column(db.Integer, db.ForeignKey('dairy_owner.dairy_id'), nullable=False)
    quantity = db.Column(db.Numeric(10, 2), nullable=False)
    price_per_unit = db.Column(db.Numeric(10, 2), nullable=False)
    total_amount = db.Column(db.Numeric(12, 2), nullable=False)

    def __repr__(self):
        return f"Transaction ID {self.transaction_id}"
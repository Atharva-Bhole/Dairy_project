from . import db
from flask import current_app as app

class SupplyTransaction(db.Model):
    __tablename__ = 'supply_transactions'
    supply_transaction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.farmer_id'))
    supply_id = db.Column(db.Integer, db.ForeignKey('supplies.supply_id'))
    quantity = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Numeric(12, 2), nullable=False)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    def __repr__(self):
        return f"Supply Transaction ID: {self.supply_transaction_id}, Farmer ID: {self.farmer_id}, Supply ID: {self.supply_id}"
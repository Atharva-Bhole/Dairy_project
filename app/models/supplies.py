from . import db
from flask import current_app as app
from app.models.supply_transaction import SupplyTransaction
class Supplies(db.Model):
    __tablename__ = 'supplies'
    supply_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dairy_id = db.Column(db.Integer, db.ForeignKey('dairy_owner.dairy_id'))
    name = db.Column(db.String(length=100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    supply_transaction = db.relationship('SupplyTransaction', backref='Supplies', lazy=True)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    def __repr__(self):
        return f"Supply Name: {self.name}, Supply ID: {self.supply_id}"
from . import db
from flask import current_app as app
from sqlalchemy import Sequence

class farmer_bank_details(db.Model):
    __tablename__ = 'farmer_bank_details'
    farmer_id = db.Column(db.String, db.ForeignKey('farmers.farmer_id'))
    account_no = db.Column(db.Integer, primary_key=True)
    ifsc_code = db.Column(db.String)
    bank_name = db.Column(db.String)
    
    def as_dict(self):
        return {
            'farmer_id': self.farmer_id,
            'account_no': self.account_no,
            'ifsc_code': self.ifsc_code,
            'bank_name': self.bank_name,
        }

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    def __repr__(self):
        return f"farmer Id {self.farmer_id}"

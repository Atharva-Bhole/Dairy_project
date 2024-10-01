from . import db
from flask import current_app as app
from sqlalchemy import Sequence

class farmer_bank_details(db.Model):
    __tablename__ = 'farmer_bank_details'
    farmer_id = db.Column(db.String, primary_key=True)
    account_no = db.Column(db.Integer)
    ifsc_code = db.Column(db.String)
    bank_name = db.Column(db.String)

    def __repr__(self):
        return f"farmer Id {self.farmer_id}"

from . import db 
from flask import current_app as app 

class muster(db.Model):
    __tablename__ = 'muster'
    farmer_id = db.Column(db.Integer(), db.ForeignKey('farmers.farmer_id'))
    milk_union = db.Column(db.String())
    muster_id = db.Column(db.Integer())
    payment_period_start = db.Column(db.Date)
    payemnt_period_end = db.Column(db.Date)
    district = db.Column(db.String())
    taluka = db.Column(db.String())
    village = db.Column(db.String())
    bulk_milk_supplier = db.Column(db.String())
    farmer_name = db.Column(db.String(), db.ForeignKey('farmers.name'))
    total_milk = db.Column(db.Numeric(10,2))
    percent_fat = db.Column(db.Numeric(10,2))
    percent_snf = db.Column(db.Numeric(10,2))
    amount = db.Column(db.Numeric(10,2))
    deduction_amount = db.Column(db.Numeric(10,2))
    final_amount_after_deduction = db.Column(db.Numeric(10,2))
    avg_rate_per_litre = db.Column(db.Numeric(10,2))

    def __repr__(self):
        return f"Muster ID {self.muster_id}"
    
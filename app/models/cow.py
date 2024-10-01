from . import db
from flask import current_app as app 

class cows(db.Model):
    __tablename__ = 'cows'
    animal_id = db.Column(db.Integer(), primary_key = True)
    cow_breed = db.Column(db.String())
    gender = db.Column(db.String())
    farmer_id = db.Column(db.Integer(), db.ForeignKey('farmers.farmer_id'))
    is_milking = db.Column(db.Boolean())
    percent_fat = db.Column(db.Numeric(10,2))
    percent_snf = db.Column(db.Numeric(10,2))
    hygiene_rating = db.Column(db.Numeric())
    milking_performace = db.Column(db.Numeric())
    
from . import db
from flask import current_app as app 

class cows(db.Model):
    __tablename__ = 'cows'
    animal_id = db.Column(db.Integer(), primary_key = True)
    cow_breed = db.Column(db.String())
    gender = db.Column(db.String())
    farmer_id = db.Column(db.Integer(), foreign_key = 'farmers.farmer_id')
    is_milking = db.Column(db.Boolean())
    
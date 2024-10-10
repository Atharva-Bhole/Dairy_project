from . import db
from flask import current_app as app 

class cows(db.Model):
    __tablename__ = 'cows'

    # Unique animal ID given to each cow from the government
    animal_id = db.Column(db.Integer(), primary_key = True)

    # Breed of the cow
    cow_breed = db.Column(db.String())

    # LOL Gender of the cow asked by the government for record 
    gender = db.Column(db.String())

    # Farmer ID is foreign key from farmers table
    farmer_id = db.Column(db.Integer(), db.ForeignKey('farmers.farmer_id'))

    # Is the cow milking or not Boolean True or False during checkup
    is_milking = db.Column(db.Boolean())

    # Percentage of Fat present in milk while checkup
    percent_fat = db.Column(db.Numeric(10,2))

    # Percentage of SNF (Solid Not fats) present in milk during checkup
    percent_snf = db.Column(db.Numeric(10,2))

    # Hygiene Rating Given by the doctor ranging from 0.00 to 10.00 during checkup
    hygiene_rating = db.Column(db.Numeric())

    # Milking performace in Decimal from 0.00 to 10.00 given by doctor during checkup
    milking_performace = db.Column(db.Numeric())
    
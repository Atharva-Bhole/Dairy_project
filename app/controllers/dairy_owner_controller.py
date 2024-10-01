from flask import Flask, Blueprint, redirect, render_template, request, jsonify, make_response
from app.models import db
from app.models.cow import cows
from app.models.dairyowner import dairy_owner
from app.models.farmer_bank import farmer_bank_details
from app.models.farmer import farmers 
from app.models.muster_data import muster

dairy = Blueprint('dairy', __name__)

@dairy.route('/dairy_owner', methods=['POST'])
def dairy_create():
    data = request.get_json()
    new_dairy = dairy_owner(**data)
    db.session.add(new_dairy)
    db.session.commit()
    return "Dairy Owner Created Successfully"

@dairy.route('/viewdairydata', methods=['GET'])
def view_dairy_data():
    dairy_list = dairy_owner.query.all()
    dairy_data = [dairy.as_dict() for dairy in dairy_list]
    return make_response(jsonify(dairy_data))

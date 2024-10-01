from flask import Flask, Blueprint, redirect, render_template, request, jsonify
from app.models import db
from app.models.cow import cows
from app.models.dairyowner import dairy_owner
from app.models.farmer_bank import farmer_bank_details
from app.models.farmer import farmers 
from app.models.muster_data import muster

main = Blueprint('main', __name__)

@main.route('/farmers', methods=['GET'])
def get_farmers():
    farmer = farmers.query.all()
    return jsonify([farmers.as_dict() for farmers in farmer])

@main.route('/farmers', methods=['POST'])
def create_farmer():
    data = request.get_json()
    new_farmer = farmers(**data)
    db.session.add(new_farmer)
    db.session.commit()
    return (jsonify([new_farmer.as_dict()]),201,"User Inserted Successfully")


@main.route('/dairy_owner', methods=['POST'])
def dairy_create():
    data = request.get_json()
    new_dairy = dairy_owner(**data)
    db.session.add(new_dairy)
    db.session.commit()
    return "Dairy Owner Created Successfully"


from flask import Blueprint, request, jsonify, make_response
from app.models.farmer_bank import farmer_bank_details
from app.models import db

bank = Blueprint('bank_dets', __name__)
@bank.route('/get_farmer_bank', methods=["GET", 'POST'])
def getbank():
    data = request.get_json()
    bank_details = db.session.query(farmer_bank_details).filter_by(farmer_id=data['farmer_id']).all()
    bank_details_dict = [detail.as_dict() for detail in bank_details]
    return make_response(jsonify({"bank Details": bank_details_dict}), 200)

@bank.route('/add_farmer_bank', methods=['POST'])
def addbank():
    data = request.get_json()
    new_data = farmer_bank_details(**data)
    db.session.add(new_data)
    db.session.commit()
    return jsonify([new_data.as_dict()]), 201

@bank.route('/get_all_farmer_bank', methods=['GET'])
def get_all_farmer_bank():
    bank = farmer_bank_details.query.all()
    bank_details = [dets.as_dict() for dets in bank]
    return make_response(jsonify({"Farmer Bank Details" : bank_details}), 200)


@bank.route("/delete_farmer_bank", methods=['DELETE'])
def delete_farmer_bank():
    data = request.get_json()
    account_no = data['account_no']
    bank_details = db.session.query(farmer_bank_details).filter_by(account_no=account_no).first()
    db.session.delete(bank_details)
    db.session.commit()
    return make_response(jsonify({"message" : "Farmer Bank Details Deleted Successfully"}), 200)
from flask import Blueprint, jsonify, make_response, request
from app.models import db
from app.models.transactions import Transaction
payment_transaction = Blueprint('payment_transaction', __name__)

@payment_transaction.route("/get_transaction_data_for_farmer", methods=['GET'])
def getTransactionDataForFarmer():
    data = request.get_json()
    farmer_id = data['farmer_id']
    transaction_data = db.session.query(Transaction).filter_by(farmer_id=farmer_id).all()
    transaction_list = [dets.as_dict() for dets in transaction_data]
    return make_response(jsonify({f"Transaction Data for Farmer {farmer_id}" : transaction_list}))

@payment_transaction.route('/register_transaction_details', methods=['POST'])
def registerTransactionDetailsOfFarmer():
    data = request.get_json()
    new_transaction = Transaction(**data)
    db.session.add(new_transaction)
    db.session.commit()
    return make_response(jsonify({"Transaction Inserted Successfully" : new_transaction}))

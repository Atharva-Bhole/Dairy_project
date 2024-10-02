from flask import Blueprint, jsonify, make_response, request
from app.models import db 
from app.models.supply_transaction import SupplyTransaction
supply_transaction = Blueprint("supply_transaction", __name__)

@supply_transaction.route("/get_all_supply_transactions", methods=['GET'])
def GetAllSupplyTransactions():
    supply_transaction_data = SupplyTransaction.query.all()
    supply_trans_details = [dets.as_dict() for dets in supply_transaction_data]
    return make_response(jsonify({"Supply Transactions" : supply_trans_details}), 200)

@supply_transaction.route("/insert_supply_transaction", methods=['POST'])
def InsertSupplyTransaction():
    data = request.get_json()
    new_supply_transaction = SupplyTransaction(**data)
    db.session.add(new_supply_transaction)
    db.session.commit()
    return make_response(jsonify({"message" : "New Supply Transaction Inserted", "transaction_details" : new_supply_transaction.as_dict()}))

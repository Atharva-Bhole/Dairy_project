from flask import Blueprint, jsonify, make_response, request
from app.models import db
from app.models.supplies import Supplies

supplies = Blueprint('supplies', __name__)

@supplies.route('/get_supplies', methods=['GET'])
def get_supplies():
    data = request.get_json()
    supply_id = data['supply_id']
    if supply_id == None:
        return jsonify("Supply Id not Found in data"),404
    supply_data = db.session.query(Supplies).filter_by(supply_id = supply_id).all()
    supply_dets = [dets.as_dict() for dets in supply_data]
    return make_response(jsonify({"Supply Details" : supply_dets}),200)


@supplies.route("/get_all_supplies", methods=['GET'])
def get_all_supplies():
    supply = Supplies.query.all()
    supply_dets = [dets.as_dict() for dets in supply]
    return make_response(jsonify({"Supply Details" : supply_dets}), 200)

@supplies.route('/insert_supply_data', methods=['POST'])
def insert_supply_data():
    data = request.get_json()
    new_supply = Supplies(**data)
    db.session.add(new_supply)
    db.session.commit()
    return "Supply data inserted successfully"

@supplies.route('/delete_supply_data', methods=["DELETE"])
def delete_supply_data():
    data = request.get_json()
    supply_id = data['supply_id']
    supply_data = db.session.query(Supplies).filter_by(supply_id=supply_id).first()
    if not supply_data:
        return jsonify({"message" : "Supply Data not found"})
    db.session.delete(supply_data)
    db.session.commit()
    return jsonify({"message" : "Supply Data Deleted Successfully"})


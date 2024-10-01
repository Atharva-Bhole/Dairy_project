from flask import Blueprint, jsonify, make_response, request
from app.models import db
from app.models.farmer import farmers

farmer_bp = Blueprint("farmers", __name__)

@farmer_bp.route('/test', methods=["GET"])
def test():
    return make_response(jsonify({"message": "test route"}), 200)

@farmer_bp.route('/get_farmers', methods=["GET"])
def get_farmers():
    try:
        farmers_ = farmers.query.all()
        return make_response(jsonify({"farmers": farmers_}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "error getting farmers"}), 500)
    
@farmer_bp.route('/farmers', methods=['POST'])
def create_farmer():
    data = request.get_json()
    new_farmer = farmers(**data)
    db.session.add(new_farmer)
    db.session.commit()
    return (jsonify([new_farmer.as_dict()]),201,"User Inserted Successfully")

from flask import Blueprint, jsonify, make_response
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
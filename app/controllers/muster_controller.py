from flask import Blueprint, jsonify, request, make_response
from app.models import db
from app.models.muster_data import muster
muster_ = Blueprint("muster_", __name__)

@muster_.route('/get_muster_data', methods=['GET'])
def getdata():
    data = request.get_json()
    muster_data = db.session.query(muster).filter_by(farmer_id = data['farmer_id']).all()
    muster_details = [details.as_dict() for details in muster_data]
    return make_response(jsonify({"Muster Data": muster_details}),200)

@muster_.route('/insert_muster_data', methods=["POST"])
def putdata():
    data = request.get_json()
    new_m_data = muster(**data)
    db.session.add(new_m_data)
    db.session.commit()
    return jsonify([new_m_data.as_dict()]), 200
from flask import Blueprint, jsonify, make_response, request, session, render_template
from app.models import db
from app.models import farmers, muster
from app.controllers.forms.farmerform import GetFarmerDetailsForm
farmer_bp = Blueprint("farmers", __name__)

@farmer_bp.route('/test', methods=["GET"])
def test():
    return make_response(jsonify({"message": "test route"}), 200)

@farmer_bp.route('/get_farmers', methods=["GET"])
def get_farmers():
    try:
        farmers_ = farmers.query.all()
        return make_response(jsonify({"farmers": [f.as_dict() for f in farmers_]}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "error getting farmers"}), 500)
    
@farmer_bp.route('/farmers', methods=['POST'])
def create_farmer():
    data = request.get_json()
    new_farmer = farmers(**data)
    db.session.add(new_farmer)
    db.session.commit()
    return (jsonify([new_farmer.as_dict()]),201)


@farmer_bp.route("/farmer_profile", methods=['GET','POST'])
def getFarmerDetailsUsingForm():
    form = GetFarmerDetailsForm()
    form_data = []
    if form.validate_on_submit():
        farmer_id = form.farmer_id.data
        print("Farmer Id Fetched")
        farmer_details = db.session.query(farmers).filter_by(farmer_id=farmer_id)
        print("Farmer Details fetched")
        farmer_dets_list = [dets.as_dict() for dets in farmer_details]
        print("Dict Created")
        print(farmer_dets_list)
        return render_template('farmers/farmer_prof.html', form_data = farmer_dets_list, form=form)
    return render_template('farmers/farmer_prof.html', form_data = form_data, form=form) 


@farmer_bp.route("/get_farmer_muster_data", methods=['GET', 'POST'])
def getFarmerMusterData():
    form = GetFarmerDetailsForm()
    muster_data = []
    if form.validate_on_submit():
        farmer_id = form.farmer_id.data
        print("Farmer ID fetched")
        farmer_muster_data = db.session.query(muster).filter_by(farmer_id=farmer_id).all()
        print("Farmer Muster Data Fetched Successfully")
        farmer_muster_list = [dets.as_dict() for dets in farmer_muster_data]
        return render_template("farmers/farmer_muster_data.html", muster_data = farmer_muster_list, form=form)
    return render_template('farmers/farmer_muster_data.html', muster_data = muster_data, form=form)
from flask import  Blueprint, redirect, render_template, request, jsonify, make_response
from app.models import db
from app.models.dairyowner import dairy_owner

dairy = Blueprint('dairy', __name__)

@dairy.route('/create_dairy_owner', methods=['POST'])
def dairy_create():
    data = request.get_json()
    new_dairy = dairy_owner(**data)
    db.session.add(new_dairy)
    db.session.commit()
    return "Dairy Owner Created Successfully"

@dairy.route('/view_dairy_data', methods=['GET'])
def view_dairy_data():
    dairy_list = dairy_owner.query.all()
    dairy_data = [dairy.as_dict() for dairy in dairy_list]
    return make_response(jsonify(dairy_data))

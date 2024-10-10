from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, DateField, TelField, IntegerField, FieldList, FormField, SubmitField
from wtforms.validators import DataRequired
from app.controllers.forms import CattleForm
class FarmerRegister(FlaskForm):
    # Basic Information of Farmer

    fullname = StringField("Enter your Full Name", validators=[DataRequired()])
    mobile_number = TelField("Enter your mobile number", validators=[DataRequired()])
    email = EmailField("abcd@xyz.com", validators=[DataRequired()])
    dob = DateField("Select DOB", validators=[DataRequired()])
    
    # Farm Information

    farm_name = StringField("Name of your farm", validators=[DataRequired()])
    address = TextAreaField("Enter full address")
    no_of_cattle = IntegerField("Enter number of cattle")
    
    cattle = FieldList(FormField(CattleForm), min_entries=1)

    # Account Information

    bank_name = StringField("Enter bank name", validators=[DataRequired()])
    account_no = StringField("Enter Account Number", validators=[DataRequired()])
    branch_name = StringField("Enter branch name", validators=[DataRequired()])
    ifsc_code = StringField("Enter IFSC Code", validators=[DataRequired()])

    # Submit

    submit = SubmitField("Submit")
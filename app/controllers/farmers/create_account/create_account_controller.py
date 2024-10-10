from flask import Blueprint, redirect, render_template, url_for, session
from flask_mail import Message
from app import mail
from app import db
from app.models import farmers
from app.forms import FarmerRegister, validateForm
from create_account import GenerateRandomOTP
farmer_register = Blueprint("farmer_register", __name__)

@farmer_register.route("/farmer_signup", methods=["GET", "POST"])
def farmer_register():
    form = FarmerRegister()
    if form.validate_on_submit():
        
        # Basic Information 

        name = form.fullname.data
        mobile_number = form.mobile_number.data
        email = form.email.data 
        dob = form.dob.data 

        # Farm Information

        farm_name = form.farm_name.data 
        address = form.address.data 
        cattle_no = form.no_of_cattle.data 

        # Dynamic form handling of cattles

        cattle = form.cattle.data 

        # Account Information

        bank_name = form.bank_name.data 
        account_no = form.account_no.data 
        branch_name = form.branch_name.data 
        ifsc_code = form.ifsc_code.data 

        email_otp = GenerateRandomOTP()
        mobile_otp = GenerateRandomOTP()
        session['email_otp'] = email_otp
        session['mobile_otp'] = mobile_otp
        print(mobile_otp)
        session['email'] = email
        session['farmer_data'] = {
            "name" : name,
            "mobile_number": mobile_number,
            "dob": dob,
            "farm_name": farm_name,
            "address": address,
            "no_of_cattle": cattle_no,
            "cattle_uids": cattle,
            "bank_name": bank_name,
            "account_no": account_no,
            "branch_name": branch_name,
            "ifsc_code": ifsc_code
        }

        msg = Message('Your OTP Code is: ', recipients=[email])
        msg.body = f"Your OTP is {email_otp}. Please enter it to complete your registration"
        mail.send(msg)

        return redirect(url_for('farmer_register.validate_otp'))
    
    return render_template('farmer_register.html', form=form)


@farmer_register.route("/validate-otp", methods=["GET", "POST"])
def validate_otp():
    form = validateForm()
    if form.validate_on_submit():
        email_otp = form.email_otp.data
        mobile_otp = form.mobile_otp.data
        if int(email_otp) == session.get('email_otp') and int(mobile_otp) == session.get('mobile_otp'):
            # OTP is valid, proceed to insert data into the database
            farmer_data = session.get('farmer_data')
            # Insert farmer_data into the database (assuming SQLAlchemy)
            new_farmer = farmers(
                fullname=farmer_data["name"],
                mobile_number=farmer_data["mobile_number"],
                email=session['email'],
                dob=farmer_data["dob"],
                farm_name=farmer_data["farm_name"],
                address=farmer_data["address"],
                no_of_cattle=farmer_data["no_of_cattle"],
                cattle_uids=farmer_data["cattle_uids"],
                bank_name=farmer_data["bank_name"],
                account_no=farmer_data["account_no"],
                branch_name=farmer_data["branch_name"],
                ifsc_code=farmer_data["ifsc_code"]
            )
            db.session.add(new_farmer)
            db.session.commit()
            # Clear session data
            session.pop('otp', None)
            session.pop('email', None)
            session.pop('farmer_data', None)

            return redirect(url_for('success_page'))
        else:
            return "Invalid OTP. Please try again.", 400

    return render_template('validate_otp.html')

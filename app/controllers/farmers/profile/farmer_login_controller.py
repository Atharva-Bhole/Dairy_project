from flask import Blueprint, render_template, redirect, url_for
from app.controllers.forms import RegisterForm

farmer_profile = Blueprint(farmer_profile, __name__)

@farmer_profile.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        mobile = form.mobile.data
        address = form.address.data
        gender = form.gender.data
        
        if not name or not email or not password:
            print("All fields must be filled out.", "error")
            return render_template('register.html', form=form)
        
        sender = app.config.get('MAIL_USERNAME')  
        
        if sender is None:
            print("Mail sender is not configured.", "error")
            return render_template('register.html', form=form)
        
        otp = generateOTP()
         
        msg = Message(subject='Verify Your Email',
                 recipients=[email])
        msg.body = f"This mail is for verification please enter the otp {otp} on the page"
        try:
           app.mail.send(msg)
           print("Mail sent")
           print(otp)
           session['name'] = name
           session['email'] = email
           session['gender'] = gender
           session['password'] = password
           session['mail_otp'] = otp
           session['mobile'] = mobile
           session['address'] = address
           return redirect(url_for('main.verifyotp'))
        except Exception as e:
            print(f"Failed to send email: {e}", "error")
            return render_template('register.html', form=form)
    else:
        print("Form not validated")
    return render_template('register.html', form=form)

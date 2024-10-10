from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class validateForm(FlaskForm):
    mobile_otp = IntegerField("Enter Your Mobile OTP", validators=[DataRequired()])
    email_otp = IntegerField("Enter your Email OTP", validators=[DataRequired()])
    submit = SubmitField("Submit your OTP", validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, PasswordField, EmailField, SubmitField
class GetFarmerDetailsForm(FlaskForm):
    farmer_id = IntegerField('farmer_id', validators=[DataRequired()])
    submit = SubmitField('Get Farmer Details', validators=[DataRequired()])
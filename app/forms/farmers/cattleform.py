from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CattleForm(FlaskForm):
    uid = StringField("Enter Cattle UID", validators=[DataRequired()])
    
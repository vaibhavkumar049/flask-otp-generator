from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SimpleForm(FlaskForm):
    otp = StringField('otp', validators=[DataRequired()])
    # prev=StringField('prev')
    submit = SubmitField('Submit')
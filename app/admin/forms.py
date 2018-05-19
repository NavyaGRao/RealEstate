# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , IntegerField
from wtforms.validators import DataRequired

class HouseForm(FlaskForm):
    """
    Form for user to add or edit a house
    """
    
    type = StringField('Type', validators=[DataRequired()])
    house_num= IntegerField('House Number')
    area = StringField('Area', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    room_cnt = IntegerField('Room count', validators=[DataRequired()])
    bath_cnt = IntegerField('Bathroom count')
    amount = IntegerField('Amount' ,validators=[DataRequired()] )
    balcony = StringField('Balcony')
    utility = StringField('Utility')
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')   
    
    
class SiteForm(FlaskForm):
    
    
    type = StringField('Type', validators=[DataRequired()])
    site_num= IntegerField('Site Number')
    area = StringField('Area', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    sq_feet = IntegerField('Sq. feet')
    amount = IntegerField('Amount' ,validators=[DataRequired()] )
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
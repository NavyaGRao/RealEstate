from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField,DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import House, Site

class CityForm(FlaskForm):

    city_name = QuerySelectField(query_factory=lambda: House.query.all(),get_label="city")
    submit=SubmitField('Search')
    
class sCityForm(FlaskForm):
    city_name = QuerySelectField(query_factory=lambda: Site.query.all(),get_label="city")
    submit=SubmitField('Search')
    
class RoomForm(FlaskForm):
    room_cnt=IntegerField('Enter rooms',validators=[DataRequired()])
    submit=SubmitField('Search')
    
class AmountForm(FlaskForm):
    amount=IntegerField('Enter your Budget',validators=[DataRequired()])
    submit=SubmitField('Search')
    
class sAmountForm(FlaskForm):
    amount=IntegerField('Enter your Budget',validators=[DataRequired()])
    submit=SubmitField('Search')
    
class FeaturesForm(FlaskForm):
    features=QuerySelectField(query_factory=lambda: House.query.all(),get_label="city")
    submit=SubmitField('Search')
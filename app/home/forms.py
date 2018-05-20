from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,IntegerField,DateField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import House, Site

class CityForm(FlaskForm):

    city_name = QuerySelectField(query_factory=lambda: House.query.all(),get_label="city")
    submit=SubmitField('Search')
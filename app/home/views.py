from flask import abort,flash,redirect,url_for,render_template
from flask_login import current_user,login_required

from . import home
from .forms import CityForm
from .. import db
from ..models import House,Site
from flask import request

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Edificio")
    
@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")

@home.route('/searchpage')
def searchpage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/query/searchpage.html', title="Search")
    
@home.route('/city',methods=['GET','POST'])
def city():
    
    form = CityForm()
    if form.validate_on_submit():
        houses = db.session.query(House).filter(House.city==str(form.city_name.data)).all()
        return render_template('home/query/city.html',title="Search Form",form=form,houses=houses)
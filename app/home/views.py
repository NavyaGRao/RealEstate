from flask import abort,flash,redirect,url_for,render_template
from flask_login import current_user,login_required

from . import home
#from .forms import CityForm
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
    

    
    

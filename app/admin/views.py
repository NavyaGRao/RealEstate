# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
import sys
from . import admin
from .forms import HouseForm, SiteForm
from .. import db
from ..models import House, Site

'''def check_admin():
    if not current_user.is_admin:
        abort(403)
    """
    Prevent non-admins from accessing the page
    """
    
'''
# House Views

@admin.route('/houses', methods=['GET', 'POST'])
@login_required
def list_houses():
    """
    List all departments
    """
    #check_admin()

    houses = House.query.all()

    return render_template('admin/houses/houses.html',houses=houses, title="Houses")

@admin.route('/houses/add', methods=['GET', 'POST'])
@login_required
def add_house():
    """
    Add a house to the database
    """
    #check_admin()

    add_house = True

    form = HouseForm()
    if form.validate_on_submit():
        print(form.type.data)
        house = House(type=str(form.type.data),
                        house_num=int(form.house_num.data),
                        area=str(form.area.data),
                        city=str(form.city.data),
                        room_cnt=int(form.room_cnt.data),
                        bath_cnt=int(form.bath_cnt.data),
                        amount=int(form.amount.data),
                        balcony=int(form.balcony.data),
                        utility=int(form.utility.data),
                        description=str(form.description.data),
                        owner_id=1)
        try:
            # add house to the database
            print(db)
            db.session.add(house)
            print("%%%%%%%%%%%%%%%%%%%%%%%%%") 
            db.session.commit()
            print("jnfihdnskhsuiahka")
       
            flash('You have successfully added a new House.')
        except:
            # in case house name already exists
            flash('Error: house name already exists.')

        # redirect to houses page
        return redirect(url_for('admin.list_houses'))

    # load house template
    return render_template('admin/houses/house.html', action="Add",add_house=add_house, form=form,title="Add House")

@admin.route('/houses/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_house(id):
    """
    Edit a house
    """
   # check_admin()

    add_house = False

    house = House.query.get_or_404(id)
    form = HouseForm(obj=house)
    if form.validate_on_submit():
        house.type=form.type.data
        house.house_num=form.house_num.data
        house.area=form.area.data
        house.city=form.city.data
        house.room_cnt=form.room_cnt.data
        house.bath_cnt=form.bath_cnt.data
        house.amount=form.amount.data
        house.balcony=int(form.balcony.data)
        house.utility=int(form.utility.data)
        house.description=form.description.data
        db.session.add(house)
        print("%K%%%%%%%%%%%%%%%%%%")
        db.session.commit()
        flash('You have successfully edited the house.')

        # redirect to the departments page
        return redirect(url_for('admin.list_houses'))


    return render_template('admin/houses/house.html', action="Edit",add_house=add_house, form=form,house=house, title="Edit House")

@admin.route('/houses/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_house(id):
    """
    Delete a de from the database
    """
    #check_admin()

    house = House.query.get_or_404(id)
    db.session.delete(house)
    db.session.commit()
    flash('You have successfully deleted the house.')

    # redirect to the departments page
    return redirect(url_for('admin.list_houses'))

    return render_template(title="Delete House")
    
# Site Views

@admin.route('/sites', methods=['GET', 'POST'])
@login_required
def list_sites():
    """
    List all departments
    """
    #check_admin()

    sites = Site.query.all()

    return render_template('admin/sites/sites.html',sites=sites, title="Sites")

@admin.route('/sites/add', methods=['GET', 'POST'])
@login_required
def add_site():
    """
    Add a house to the database
    """
    #check_admin()

    add_site = True

    form = SiteForm()
    if form.validate_on_submit():
        print(form.type.data)
        site = Site(type=str(form.type.data),
                        site_num=int(form.site_num.data),
                        area=str(form.area.data),
                        city=str(form.city.data),
                        sq_feet = int(form.sq_feet.data),
                        amount=int(form.amount.data),
                        
                        description=str(form.description.data),
                        owner_id=1)
        try:
            # add house to the database
            print(db)
            db.session.add(site)
            print("%%%%%%%%%%%%%%%%%%%%%%%%%") 
            db.session.commit()
            print("jnfihdnskhsuiahka")
       
            flash('You have successfully added a new Site.')
        except:
            # in case house name already exists
            flash('Error: site name already exists.')

        # redirect to houses page
        return redirect(url_for('admin.list_sites'))

    # load house template
    return render_template('admin/sites/site.html', action="Add",add_site=add_site, form=form,title="Add Site")

@admin.route('/sites/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_site(id):
    """
    Edit a house
    """
   # check_admin()

    add_site = False

    site = Site.query.get_or_404(id)
    form = SiteForm(obj=site)
    if form.validate_on_submit():
        site.type=form.type.data
        site.site_num=form.site_num.data
        site.area=form.area.data
        site.city=form.city.data
        site.sq_feet=form.sq_feet.data
        site.amount=form.amount.data
        
        site.description=form.description.data
        db.session.add(site)
        print("%K%%%%%%%%%%%%%%%%%%")
        db.session.commit()
        flash('You have successfully edited the site.')

        # redirect to the departments page
        return redirect(url_for('admin.list_sites'))


    return render_template('admin/sites/site.html', action="Edit",add_site=add_site, form=form,site=site, title="Edit Site")

@admin.route('/sites/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_site(id):
    """
    Delete a de from the database
    """
    #check_admin()

    site = Site.query.get_or_404(id)
    db.session.delete(site)
    db.session.commit()
    flash('You have successfully deleted the Site.')

    # redirect to the departments page
    return redirect(url_for('admin.list_sites'))

    return render_template(title="Delete Site")
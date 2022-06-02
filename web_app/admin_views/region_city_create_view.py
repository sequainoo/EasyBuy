#!/usr/bin/python3
"""definition of Region and City creation  functions"""

import os

from flask import render_template, request, flash
from sqlalchemy.exc import IntegrityError

from web_app.admin_views import admin_views
from models import storage, Region, City
from utilities.small_helpers import uuid4


@admin_views.route('/create-region',
                   methods=['GET','POST'],
                   strict_slashes=False)
def region_create_view():
    """Gives a region form and creates a Region an image for a phone.
    """

    # get all regions
    regions = storage.all('region')

    # return region and city creation form if request is GET
    if request.method == 'GET':
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())

    # check region name is provided
    if 'name' not in request.form:
        flash('provide name')
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())

    region_name = request.form.get('name').title()
    region = Region(name=region_name)
    # make sure there are no duplicate names for region
    try:
        storage.add(region)
        storage.save()
        flash('successful')
    except IntegrityError:
        flash('Region with such name already exists')
        storage.rollback()
    finally:
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())


@admin_views.route('/create-city',
                   methods=['GET','POST'],
                   strict_slashes=False)
def city_create_view(phone_id=''):
    """Gives a city form and creates a Region an image for a phone.
    """

    regions = storage.all('region')

    if request.method == 'GET':
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())

    if 'name' not in request.form\
        or 'region_id' not in request.form:
        flash('provide name or select region')
        return render_template('admin/region_city_create_form.html',
                               regions=regions)

    region_id = request.form.get('region_id')
    city_name = request.form.get('name').title()
    region = storage.get('region', region_id)
    if not region:
        flash('Region does not exists')
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())
    city = City(name=city_name)
    city.region = region
    try:
        storage.add(city)
        storage.save()
        flash('successful')
    except IntegrityError:
        flash('City with such name already exists')
        storage.rollback()
    finally:
        return render_template('admin/region_city_create_form.html',
                               regions=regions,
                               id=uuid4())

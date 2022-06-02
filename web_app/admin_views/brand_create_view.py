#!/usr/bin/python3
"""definition of Image upload view for a product """

from flask import render_template, request, flash, url_for, redirect

from web_app.admin_views import admin_views
from models import storage, PhoneBrand as Brand


@admin_views.route('/create-brand',
                   methods=['GET','POST'],
                   strict_slashes=False)
def brand_create_view():
    """Create a phone brand"""

    if request.method == 'GET':
        return render_template('admin/brand_create_form.html')

    # get name of brand from form data sent
    brand_name = request.form.get('name', None)

    # if its empty dont proceed
    if not brand_name:
        flash('Provide name of brand')
        return redirect(request.url)

    # incase name of brand fully a number return 
    try:
        int(brand_name)
        float(brand_name)
        flash('Brand name of wrong type')
        return redirect(request.url)
    except Exception:
        pass
    
    # create brand
    brand = Brand(name=brand_name.capitalize())
    storage.add(brand)
    try:
        # commit or save brand
        storage.save()
    except Exception:
        # if there is any integrity error such as same brand name rollback
        storage.rollback()
    flash('succesful')
    return redirect(request.url)

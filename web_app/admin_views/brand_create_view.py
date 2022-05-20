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

    brand_name = request.form.get('name', None)

    if not brand_name:
        flash('Provide name of brand')
        return redirect(request.url)
    try:
        int(brand_name)
        float(brand_name)
    except Exception:
        pass
    else:
        flash('Brand name of wrong type')
        return redirect(request.url)
    
    brand = Brand(name=brand_name.capitalize())
    storage.add(brand)
    try:
        storage.save()
    except Exception:
        storage.rollback()
    flash('succesful')
    return redirect(request.url)

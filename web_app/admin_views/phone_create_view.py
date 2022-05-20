#!/usr/bin/python3
"""definition of phone creation and its image upload views"""

from flask import render_template, request, flash, redirect, url_for

from web_app.admin_views import admin_views
from models import storage, Phone


@admin_views.route('/create-phone', methods=['GET', 'POST'], strict_slashes=False)
def phone_create_view():
    """Allows to create a phone.
    On GET it returns a page with forms to create product and upload images
    """
    if request.method == 'GET':
        brands = storage.all('phone-brand')
        return render_template('admin/create_phone.html', brands=brands)
    if request.method == 'POST':
        name = request.form.get('name', None)
        brand_id = request.form.get('brand_id', None)
        quantity = request.form.get('quantity', 1)
        price = request.form.get('price', None)
        description = request.form.get('description', None)

        if not name or not brand_id or not price or not description:
            flash('Provide neccessary details')
            return redirect(request.url)

        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            flash('Quantity and price should be numeric')
            return redirect(request.url)

        if not storage.get('phone-brand', brand_id):
            flash('Select a valid brand')
            return redirect(request.url)

        phone = Phone(name=name, brand_id=brand_id, quantity=quantity,
                      price=price, description=description)
        storage.add(phone)
        storage.save()
        return redirect(url_for('admin_views.image_upload_view',
                                phone_id=phone.id))

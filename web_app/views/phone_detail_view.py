#!/usr/bin/python3
"""definition of detailed view of a phone page view"""

from flask import render_template, redirect, url_for

from web_app.views import app_views
from models import storage
from utilities.small_helpers import uuid4


@app_views.route('/phones/<id_>', strict_slashes=False)
def product_detail_view(id_):
    """Returns the product detail page"""
    phone = storage.get('Phone', id_)
    if not phone:
        return redirect(url_for('app_views.phone_list_view'))
    quantity = [qty + 1 for qty in range(0, phone.quantity)]
    id = uuid4()

    return render_template('phone_detail.html', phone=phone,
                           quantity=quantity, id=id)

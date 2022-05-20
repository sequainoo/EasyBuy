#!/usr/bin/python3
"""definition of detailed view of a product page view"""

from flask import render_template

from web_app.views import app_views
from models import storage
from utilities.small_helpers import uuid4


@app_views.route('/products/<id_>', strict_slashes=False)
def product_detail_view(id_):
    """Returns the product detail page"""
    phone = storage.get('Phone', id_)
    quantity = [qty + 1 for qty in range(0, phone.quantity)]
    id = uuid4()

    return render_template('product_detail.html', phone=phone,
                           quantity=quantity, id=id)

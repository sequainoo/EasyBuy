#!/usr/bin/python3
"""definition of detailed view of a product page view"""

from flask import render_template

from web_app.views import app_views
from models import storage


@app_views.route('/products/<id>', strict_slashes=False)
def product_detail_view(id_):
    """Returns the product detail page"""
    product = storage.get('Product', id_)

    return render_template('product_detail.html', product=product)

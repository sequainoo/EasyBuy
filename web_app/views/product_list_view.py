#!/usr/bin/python3
"""definition of home page view"""

from flask import render_template

from web_app.views import app_views
from models import storage


@app_views.route('/products', strict_slashes=False)
def product_list_view():
    """Returns the products page populated with a list of products"""
    products = storage.all('Product')
    brands = storage.all('Brand')

    return render_template('product_list.html', products=products, brands=brands)

#!/usr/bin/python3
"""definition of home page view"""

from flask import render_template

from web_app.views import app_views
from models import storage


@app_views.route('/phones', strict_slashes=False)
def phone_list_view():
    """Returns the products page populated with a list of products"""
    phones = storage.all('Phone')
    brands = storage.all('phone-brand')

    return render_template('phone_list.html', phones=phones, brands=brands)

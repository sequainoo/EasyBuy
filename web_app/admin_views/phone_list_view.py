#!/usr/bin/python3
"""definition of Image upload view for a product """

from flask import render_template, request, flash, url_for, redirect
from sqlalchemy import text

from web_app.admin_views import admin_views
from models import storage
from utilities.small_helpers import uuid4


@admin_views.route('/list-phones', strict_slashes=False)
def phone_list_view():
    """List phones for admin"""

    phones = storage.all('phone')

    return render_template('admin/phone_list.html',
                               phones=phones, id=uuid4())
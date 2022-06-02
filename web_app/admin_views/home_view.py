#!/usr/bin/python3
"""Defines admin Home view """

from flask import render_template

from web_app.admin_views import admin_views


@admin_views.route('/', strict_slashes=False)
def home_view():
    """Return admin homepage"""

    return render_template('admin/home.html')
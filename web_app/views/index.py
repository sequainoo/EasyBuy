from web_app.views import app_views
from flask import render_template, request, redirect, url_for

from models import storage
from utilities.small_helpers import uuid4


@app_views.route('/')
def index():
    """Landing page render"""
    return render_template('landing.html', id=uuid4())

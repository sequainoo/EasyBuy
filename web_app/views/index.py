from web_app.views import app_views
from flask import render_template, request, redirect, url_for

from models import storage
from utilities.small_helpers import uuid4
@app_views.route('/')
def index():
    request.phones = storage.all('phone')
    request.brands = storage.all('phone-brand')
    return redirect(url_for('app_views.product_list_view'))

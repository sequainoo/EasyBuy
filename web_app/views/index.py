from web_app.views import app_views
from flask import render_template, request

from models import storage
from utilities.small_helpers import uuid4
@app_views.route('/')
def index():
    request.phones = storage.all('phone')
    request.brands = storage.all('phone-brand')
    return render_template('base.html', id=uuid4())
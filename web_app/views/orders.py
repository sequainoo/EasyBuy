from web_app.views import app_views
from flask import render_template, request, redirect, url_for

from models import storage
from utilities.small_helpers import uuid4


@app_views.route('/orders', methods=['POST'])
def orders_view():
    """Shows a list of orders by email
    """
    email = request.form.get('email', '')
    if not email:
        return redirect(url_for('app_views.phone_list'))
    orders = storage.get_orders_by_email(email)
    return render_template('orders.html', orders=orders, id=uuid4())

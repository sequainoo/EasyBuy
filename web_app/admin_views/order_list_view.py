#!/usr/bin/python3
"""definition of Image upload view for a product """

from flask import render_template, request, flash, url_for, redirect
from sqlalchemy import text

from web_app.admin_views import admin_views
from models import storage
from utilities.small_helpers import uuid4


@admin_views.route('/list-orders',
                   methods=['GET','POST'],
                   strict_slashes=False)
def order_list_view():
    """Create a phone brand"""

    orders = storage.all('order')

    if request.method == 'GET':
        return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())

    if not request.form:
        return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())
    if 'paid' in request.form and 'notpaid' not in request.form:
        orders = orders.filter(text('orders.paid is true'))
    if 'notpaid' in request.form and 'paid' not in request.form:
        orders = orders.filter(text('orders.paid is not true'))
    if 'processed' in request.form:
        orders = orders.filter(text('orders.processed is true'))
    if 'notprocessed' in request.form:
        orders = orders.filter(text('orders.processed is not true'))
    if 'shipped' in request.form:
        orders = orders.filter(text('orders.shipped is true'))
    if 'notshipped' in request.form:
        orders = orders.filter(text('orders.shipped is not true'))
    return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())
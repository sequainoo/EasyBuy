#!/usr/bin/python3
"""definition of order list function."""

from flask import render_template, request, flash, url_for, redirect
from sqlalchemy import text

from web_app.admin_views import admin_views
from models import storage
from utilities.small_helpers import uuid4


@admin_views.route('/list-orders',
                   methods=['GET','POST'],
                   strict_slashes=False)
def order_list_view():
    """Display a list of orders for the admin"""

    # get all orders
    orders = storage.all('order')

    # return all orders for first request here with GET
    if request.method == 'GET':
        return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())

    # post request means we are filtering these orders by some keys

    # if no data is in the form send all orders
    if not request.form:
        return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())
    # incase paid and not paid are what to filter for return all objects
    # as all orders are either paid or not paid
    # but if paid or not paid is exclusive then return the order filtered
    # either one included
    if 'paid' in request.form and 'notpaid' not in request.form:
        orders = orders.filter(text('orders.paid is true'))
    if 'notpaid' in request.form and 'paid' not in request.form:
        orders = orders.filter(text('orders.paid is not true'))
    # include all processed orders
    if 'processed' in request.form:
        orders = orders.filter(text('orders.processed is true'))
    # include all not processed orders
    if 'notprocessed' in request.form:
        orders = orders.filter(text('orders.processed is not true'))
    # include all shipped orders
    if 'shipped' in request.form:
        orders = orders.filter(text('orders.shipped is true'))
    # include all notshipped
    if 'notshipped' in request.form:
        orders = orders.filter(text('orders.shipped is not true'))
    return render_template('admin/order_list.html',
                               orders=orders, id=uuid4())

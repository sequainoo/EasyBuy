#!/usr/bin/python3
"""definition of a view that marks an order as processed"""

from flask import flash, url_for, redirect

from web_app.admin_views import admin_views
from models import storage


@admin_views.route('/process-order/<order_id>', strict_slashes=False)
def process_order_view(order_id=''):
    """Marks an order as processed"""

    if not order_id:
        flash('Supply an order id!')
        return redirect(url_for('admin_views.order_list_view'))
    order = storage.get('order', order_id)

    if not order:
        flash('Order does not exist!')
        return redirect(url_for('admin_views.order_list_view'))

    if not order.paid:
        flash('Order has not been paid for, cannot mark it for processing!')
        return redirect(url_for('admin_views.order_list_view'))

    if order.processed:
        flash('Order is already Processed!')
        return redirect(url_for('admin_views.order_list_view'))

    order.processed = True
    storage.add(order)
    storage.save()

    flash('Order marked as processed!')
    return redirect(url_for('admin_views.order_list_view'))

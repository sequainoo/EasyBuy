#!/usr/bin/python3
"""definition of view that marks order as shipped """

from flask import flash, url_for, redirect

from web_app.admin_views import admin_views
from models import storage


@admin_views.route('/ship-order/<order_id>', strict_slashes=False)
def ship_order_view(order_id=''):
    """Marks an order as shipped"""

    if not order_id:
        flash('Supply an order id')
        return redirect(url_for('admin_views.order_list_view'))
    order = storage.get('order', order_id)

    if not order:
        flash('Order does not exist')
        return redirect(url_for('admin_views.order_list_view'))

    if order.shipped:
        flash('Order is already Shipped!')
        return redirect(url_for('admin_views.order_list_view'))

    if not order.paid:
        flash('Order has not been paid for cannot mark it as shipped')
        return redirect(url_for('admin_views.order_list_view'))

    if not order.processed:
        flash('Order is not Processed Yet')
        return redirect(url_for('admin_views.order_list_view'))

    order.shipped = True
    storage.add(order)
    storage.save()

    flash('Order marked as shipped successfully')
    return redirect(url_for('admin_views.order_list_view'))

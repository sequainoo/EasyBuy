#!/usr/bin/python3
"""Defines a view to generate a page for a cart"""

from flask import render_template, request, redirect, url_for

from web_app.views import app_views
from models import storage
from utilities.small_helpers import uuid4


@app_views.route('/cart', methods=['GET'], strict_slashes=False)
def cart_detail_view():
    """Returns a Cart page.

    Expects Query String in the format /cart?id=qty&id1=qty..:
        id (str): id of phone to purchase.
        qty (int): quantity of the phone.

    Return:
        The cart page with either None as cart data or
        the cart data if it was sent in a format specified as above
    """
    cart = request.args

    # if no cart data is passed return to the phone list page
    if not cart:
        return redirect(url_for('app_views.phone_list_view'))

    # iterate over each phone id and quantity pair,
    # obtain phone object from database with id and
    # build phones_quantities list as a tuple of phone object
    # and quantity.
    # Check for bad data and when found return to phones page

    phones_quantities = []
    for id, qty in cart.items():
        try:
            qty = int(qty)
            phone = storage.get('phone', id)
            if not phone:
                raise ValueError
            phones_quantities.append(phone, qty)
        except (ValueError, TypeError):
            return redirect(url_for('app_views.phone_list_view'))

    # render cart page with phones_quantities list
    return render_template('cart.html',
                           phones_quantities=phones_quantities,
                           id=uuid4())

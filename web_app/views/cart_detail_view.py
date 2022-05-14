#!/usr/bin/python3
"""Cart view Definition"""

from flask import render_template, request

from web_app.views import app_views
from models import storage


@app_views.route('/cart', methods=['POST'], strict_slashes=False)
def cart_view(id_):
    """Returns a Cart page.

    Cart data format:
        {
            "cart": {
                "<product_id_0>": quantity,
                "<product_id_1>": quantity,
                ...
            }
        }

    Renders:
        The cart page with either None as cart data or
        the cart data if it was sent in a format specified as above
    """
    cart = request.get_json()

    if cart:
        cart = cart.get('cart', None)
    return render_template('cart.html', cart=cart)

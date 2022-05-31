#!/usr/bin/python3
"""Cart view Definition"""

from flask import render_template, request, redirect, url_for

from web_app.views import app_views
from models import storage
from utilities.small_helpers import uuid4

# @app_views.route('/cart', methods=['POST'], strict_slashes=False)
# def cart_detail_view():
#     """Returns a Cart page.

#     Cart data format:
#         {
#             "cart": {
#                 "<product_id_0>": quantity,
#                 "<product_id_1>": quantity,
#                 ...
#             }
#         }
#     As Query String:
#     ?id=qty&id1=qty..

#     Renders:
#         The cart page with either None as cart data or
#         the cart data if it was sent in a format specified as above
#     """
#     cart = request.get_json()

#     if cart:
#         cart = cart.get('cart', None)
#     if not cart:
#         return redirect(url_for('app_views.product_list_view'))
#     phones_quantities = []
#     for id, qty in cart.items():
#         phones_quantities.append((storage.get('phone', id), int(qty)))
#     print(phones_quantities)
#     return render_template('cart.html', phones_quantities=phones_quantities)


@app_views.route('/cart', methods=['GET'], strict_slashes=False)
def cart_detail_view():
    """Returns a Cart page.

    As Query String:
        /cart?id=qty&id1=qty..

    Renders:
        The cart page with either None as cart data or
        the cart data if it was sent in a format specified as above
    """
    cart = request.args

    if not cart:
        return redirect(url_for('app_views.phone_list_view'))
    phones_quantities = []
    for id, qty in cart.items():
        try:
            qty = int(qty)
            phones_quantities.append((storage.get('phone', id), qty))
        except (ValueError, TypeError):
            return redirect(url_for('app_views.phone_list_view'))
    return render_template('cart.html',
                           phones_quantities=phones_quantities,
                           id=uuid4())

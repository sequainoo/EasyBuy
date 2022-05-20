#!/usr/bin/python3
"""Checkout view Definition"""

from flask import render_template, request, jsonify, url_for

from web_app.views import app_views
from models import storage, Order, OrderItem, Customer

from utilities.small_helpers import uuid4


@app_views.route('/checkout', methods=['POST'], strict_slashes=False)
def checkout_view():
    """Checkout checks out cart item

    checkout information format:
        {
            "cart": {
                "<product_id_0>": quantity (int),
                "<product_id_1>": quantity (int),
                ...
            },
            "email": "<email_of_user>",
            "first_name": "<first name(s)>",
            "last_name": "<last name(s)>",
        }

    Return:
        An Order page with order summary, address collection form,
        payment collection_form.

        If no cart or is empty cart then error as json is sent.
    """
    print(request.data)
    # retrieve checkout information
    checkout_info = request.get_json()

    # in case information is bad, return a bad request(400) response
    if not checkout_info or not checkout_info.get('cart', None)\
        or not checkout_info.get('email', None):
        return jsonify({'error': 'cart or email is empty'}), 400

    customer = storage.get_customer_by_email(checkout_info.get('email'))
    # if custommer is does not exist with such an email
    # then check customer provides first_name and last_name
    if not customer and (not checkout_info.get('first_name', None)
        or not checkout_info.get('last_name', None)):
        return jsonify({'error': 'first_name or last_name is required '}), 400

    # verify items to purchase exists
    # and the quantity of each does not exceed what is in stock
    order_items = checkout_info.get('cart').items()
    for id_, quantity in order_items:
        phone = storage.get('Phone', id_)
        if not phone:
            return render_template('error404.html'), 404
        if (phone.quantity - quantity) < 0:
            return jsonify({'error': 'Quanity is above what is in stock'}), 400

    # create an order, add its related items
    order = Order(number_of_items=0, total_cost=0.00)
    for id_, quantity in order_items:
        phone = storage.get('Phone', id_)
        order_item = OrderItem(phone_id=id_,
                               quantity_ordered=quantity,
                               unit_cost=phone.price,
                               total_cost=round(quantity * phone.price))
        order.number_of_items += quantity
        order.total_cost += order_item.total_cost
        order.items.append(order_item)

    # create a customer but with no account and an associated order
    email = checkout_info.get('email')
    first_name = checkout_info.get('first_name')
    last_name = checkout_info.get('last_name')

    # if customer does not exists create a new customer else use existing
    if not customer:
        customer = Customer(email=email,
                            first_name=first_name,
                            last_name=last_name)
    customer.orders.append(order)

    # Add to storage and save
    storage.add(customer)
    storage.save()

    regions = storage.all('region')
    cities = storage.all('city')
    # return render_template('checkout.html',
    #                        order=order,
    #                        customer=customer,
    #                        regions=regions,
    #                        cities=cities)
    return jsonify({
        'url': url_for('app_views.checkout_existing_order_view',
                       order_id=order.id)
        })


@app_views.route('/checkout/<order_id>')
def checkout_existing_order_view(order_id=''):
    """Gives a page to make payment for an existing order if not paid"""
    order = storage.get('Order', order_id)

    if not order:
        return render_template('404_page.html'), 404

    if not order.paid:
        regions = storage.all('region')
        cities = storage.all('city')
        return render_template('checkout.html',
                               order=order,
                               customer=order.customer,
                               regions=regions,
                               cities=cities,
                               id=uuid4())
    return redirect(url_for('app_views.product_list_view'))

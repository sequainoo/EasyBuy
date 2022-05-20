#!/usr/bin/python3
"""Payment view Definition"""

from datetime import date, datetime, timedelta
import random

from flask import render_template, request, url_for, flash, jsonify

from web_app.views import app_views
from models import storage, Payment


@app_views.route('/payment', methods=['POST'], strict_slashes=False)
def cart_view():
    """Returns a Cart page.

    Post data format:
        {
            "order_id": "<order_id>",
            "details": {
                "name_on_card": "<first_name m. last_name>",
                "card_number": "<cardno>",
                "exp_year": "<year of expiry>",
                "exp_month": "<month of expiry>"
            }
        }

    Return:
        if successful return a succes page
        else unsuccessful page
    """
    payment_info = request.get_json()

    # confirm all neccessary details are provided
    if not payment_info\
        or not payment_info.get('order_id', None)\
        or not payment_info.get('details', None)\
        or not payment_info.get('details').get('name_on_card', None)\
        or not payment_info.get('details').get('card_number', None)\
        or not payment_info.get('details').get('exp_year', None)\
        or not payment_info.get('details').get('exp_month', None):
        return jsonify({'error': 'missing data on payment details'}), 400

    # confirm order exists
    order = storage.get('Order', payment_info.get('order_id'))
    if not order:
        return jsonify({'error': 'Order does not exist'}), 400
    
    if not order.customer.addresses:
        return jsonify({'error': 'you need an address'}), 400

    try:
        year_now = date.today().year
        exp_year = int(payment_info.get('details').get('exp_year'))
        exp_month = int(payment_info.get('details').get('exp_month'))
    
        # confirm card year is not in the past
        # and is not more than 5 years from now
        if year_now > exp_year or (exp_year - year_now) > 5:
            return jsonify({'error': 'expiry year is not valid'}), 400

        # check month is valid mondth 1 - 12
        if  exp_month > 12 or exp_month < 1:
            return jsonify({'error': 'month is not valid'})
    except ValueError:
        return jsonify({"error": 'expiry year and month must be digits'}), 400

    # at this point card number should be validated.
    # afterwards payment is processed by api call

    # assume payment is successful or failed
    successful = random.choice([True, False])
    
    # if successful save payment details for that order
    if successful:
        payment = Payment(amount_paid=order.total_cost)
        order.payment = payment

        # mark order as paid and set shipping date to today + 1 day
        order.paid = True
        order.shipping_date = datetime.now() + timedelta(days=1)
        storage.add(payment)
        storage.save()

        # notify customer by email, sending the order url to see status

        # return a payment successful page
        flash('Payment Successful order is being processed!')
        return render_template('payment_successful.html')
    else:
        flash('Payment failed !')
        url = url_for('app_views.checkout_existing_order_view',
                      order_id=order.id)
        return render_template('payment_failed.html', order_url=url)
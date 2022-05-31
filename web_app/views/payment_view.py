#!/usr/bin/python3
"""Payment view Definition"""

from datetime import date, datetime, timedelta
import os

import requests
from flask import render_template, request, url_for, flash, jsonify

from web_app.views import app_views
from models import storage, Payment


@app_views.route('/payment', methods=['POST'], strict_slashes=False)
def payment_view():
    """Verify flutterwave payment and mark order as paid, saving payment

    Receives payment_response payload from the payment made on the frontend:
        {
            "status": "successful",
            "tx_ref": "titanic-48981487343MDI0NzMx",
            "transaction_id": 495000,
            "order_id": "sdasfe..."
        }

    verification endpoint returns this for success:
        {
            "status": "success",
            "message": "Transaction fetched successfully",
            "data": {
                "id": 1163068,
                "tx_ref": "akhlm-pstmn-blkchrge-xx6",
                "flw_ref": "FLW-M03K-02c21a8095c7e064b8b9714db834080b",
                "device_fingerprint": "N/A",
                "amount": 3000,
                "currency": "NGN",
                "charged_amount": 3000,
                "app_fee": 1000,
                "merchant_fee": 0,
                "processor_response": "Approved",
                "auth_model": "noauth",
                "ip": "pstmn",
                "narration": "Kendrick Graham",
                "status": "successful",
                "payment_type": "card",
                "created_at": "2020-03-11T19:22:07.000Z",
                "account_id": 73362,
                "amount_settled": 2000,
                "card": {
                "first_6digits": "553188",
                "last_4digits": "2950",
                "issuer": " CREDIT",
                "country": "NIGERIA NG",
                "type": "MASTERCARD",
                "token": "flw-t1nf-f9b3bf384cd30d6fca42b6df9d27bd2f-m03k",
                "expiry": "09/22"
                },
                "customer": {
                "id": 252759,
                "name": "Kendrick Graham",
                "phone_number": "0813XXXXXXX",
                "email": "user@example.com",
                "created_at": "2020-01-15T13:26:24.000Z"
                }
            }
        }
    
    Verification endpoint returns this for failaure if no transaction id as such exists:
        {
            "status": "error",
            "message": "No transaction was found for this id",
            "data": null
        }

    Return:
        if successful return {"status": "successful"}
        else {"status": "unsuccessful"}
    """
    payment_response = request.get_json()

    # confirm all neccessary details are provided
    if not payment_response\
        or not payment_response.get('order_id', None)\
        or not payment_response.get('transaction_id', None)\
        or not payment_response.get('status', None)\
        or not payment_response.get('tx_ref', None):
        return jsonify({'error': 'missing important'}), 400

    # get order and confirm order exists confirm order exists
    order = storage.get('Order', payment_response.get('order_id'))
    if not order:
        return jsonify({'error': 'Order does not exist'}), 404

    # send request to payment verification endpoint
    endpoint = 'https://api.flutterwave.com/v3/transactions/{}/verify'.format(
        payment_response['transaction_id']
    )
    authorization_value = 'Bearer {}'.format(os.getenv('FLW_SECRET_KEY'))
    response = requests.get(endpoint,
                            headers={'Authorization': authorization_value,
                                     'Content-Type': 'application/json'})
    response = response.json()

    # if no transaction is not found return to same message
    if response['status'] == 'error':
        return jsonify({'status': 'error'})

    # if transaction exists verify it has details as expected
    if response['status'] == 'success'\
        and order.transaction_reference == response['data']['tx_ref']\
        and response['data']['currency'] == 'NGN'\
        and response['data']['amount'] >= order.total_cost:

        payment = Payment(amount_paid=order.total_cost)
        order.payment = payment

        # mark order as paid and set shipping date to today + 1 day
        order.paid = True
        order.shipping_date = datetime.now() + timedelta(days=1)

        # update product quantities
        for order_item in order.items:
            order_item.phone.quantity -= order_item.quantity_ordered

        storage.add(order)
        storage.save()

        # notify customer by email, sending the order url to see status

        # return a payment successful page
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})
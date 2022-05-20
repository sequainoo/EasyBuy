#!/usr/bin/python3
"""Payment view Definition"""

import json
from datetime import date, datetime, timedelta

from flask import redirect, request, url_for, jsonify, flash
from sqlalchemy.exc import IntegrityError

from web_app.views import app_views
from models import storage, Address


@app_views.route('/address', methods=['POST'], strict_slashes=False)
def address_view():
    """Returns a Cart page.

    Post data format:
        {
            "customer_id": "<customer_id>",
            "region_id": <region_id>,
            "city_id": <city_id>,
            "town": <town>,
            "phone_number": <phone_number>
        }

    Return:
        if successful return a succes page
        else unsuccessful page
    """
    # print(request.headers)

    # data = request.get_json(force=True)
    data = request.form

    customer_id = data.get('customer_id', None)
    region_id = data.get('region_id', None)
    city_id = data.get('city_id', None)
    town = data.get('town', None)
    phone_number = data.get('phone_number', None)
    
    if not customer_id or not region_id or not city_id\
        or not town or not phone_number:
        flash('incomplete form')
        return redirect(
            url_for('app_views.checkout_existing_order_view',
            order_id=request.args['order_id'])
        )

    customer = storage.get('customer', customer_id)
    if not customer:
        return jsonify({'error': 'customer does not exist'}), 400

    if not storage.get('region', region_id):
        return jsonify({'error': 'region does not exist'}), 400

    if not storage.get('city', city_id):
        return jsonify({'error': 'city does not exist'}), 400

    if len(phone_number) < 10 or len(phone_number) > 13:
        return jsonify({'error': 'city does not exist'}), 400

    if len(customer.addresses) > 0:
        for address in customer.addresses:
            address.default = False

    address = Address(customer_id=customer_id,
                      region_id=region_id,
                      city_id=city_id,
                      town=town,
                      phone_number=phone_number)
    try:
        storage.add(address)
        storage.save()
    except IntegrityError as e:
        storage.rollback()
        flash('Address with that info exists')
        return redirect(
            url_for('app_views.checkout_existing_order_view',
            order_id=request.args['order_id'])
        )
    # return jsonify({'address_id': address.id})
    flash('Successfully added')
    return redirect(
        url_for('app_views.checkout_existing_order_view',
        order_id=request.args['order_id'])
    )

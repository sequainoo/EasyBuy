#!/usr/bin/python3
"""Defines view to create customer address"""

import json
from datetime import date, datetime, timedelta

from flask import redirect, request, url_for, jsonify, flash
from sqlalchemy.exc import IntegrityError

from web_app.views import app_views
from models import storage, Address


@app_views.route('/address', methods=['POST'], strict_slashes=False)
def address_view():
    """Creates address for a customer

    Post address_info format:
        {
            "customer_id": "<customer_id>",
            "region_id": <region_id>,
            "city_id": <city_id>,
            "town": <town>,
            "phone_number": <phone_number>
        }
    id of order is passed as querystring to return to checkout page of the
    specific order that address creation request came from.
    ?order_id=id

    Return:
        checkout page with either success or failed status message
    """
    # retrieve all address information from the form
    address_info = request.form

    customer_id = address_info.get('customer_id')
    region_id = address_info.get('region_id')
    city_id = address_info.get('city_id')
    town = address_info.get('town')
    phone_number = address_info.get('phone_number')
    
    # if validation of address info fails go back to the checkout page
    if not validate_address_info(address_info):
        return redirect(
            url_for('app_views.checkout_existing_order_view',
            order_id=request.args['order_id'])
        )

    # set old addresses of the customer to not default while new is created
    customer = storage.get('customer', customer_id)
    if len(customer.addresses) > 0:
        for address in customer.addresses:
            address.default = False

    # create address object from the valid info
    address = Address(customer_id=customer_id,
                      region_id=region_id,
                      city_id=city_id,
                      town=town,
                      phone_number=phone_number)
    try:
        storage.add(address)
        storage.save()
        storage.reload()
    except IntegrityError as e:
        storage.rollback()
        flash('Address with that info exists')
        return redirect(
            url_for('app_views.checkout_existing_order_view',
            order_id=request.args['order_id'])
        )
    flash('Successfully added')
    return redirect(
        url_for('app_views.checkout_existing_order_view',
        order_id=request.args['order_id'])
    )


def validate_address_info(address_info):
    """Validates address  information passed from the form."""
    customer_id = address_info.get('customer_id', None)
    region_id = address_info.get('region_id', None)
    city_id = address_info.get('city_id', None)
    town = address_info.get('town', None)
    phone_number = address_info.get('phone_number', None)
    
    # make sure information is right
    if not customer_id or not region_id or not city_id\
        or not town or not phone_number:
        flash('incomplete form')
        return False

    customer = storage.get('customer', customer_id)
    if not customer:
        flash('Customer not exist')
        return False

    if not storage.get('region', region_id):
        flash('Region not exist')
        return False

    if not storage.get('city', city_id):
        flash('City not exist')
        return False

    # extra checks for a valid phone would be added
    if len(phone_number) < 10 or len(phone_number) > 13:
        flash('Phone not valid')
        return False

    return True

#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_app.product_list_view import *
from web_app.product_detail_view import *
from web_app.payment_view import *
from web_app.checkout_view import *
from web_app.cart_detail_view import *
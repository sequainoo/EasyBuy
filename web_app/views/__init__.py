#!/usr/bin/python3

from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from web_app.views.phone_list_view import *
from web_app.views.phone_detail_view import *
from web_app.views.payment_view import *
from web_app.views.checkout_view import *
from web_app.views.cart_detail_view import *
from web_app.views.index import *
from web_app.views.address_view import *
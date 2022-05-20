#!/usr/bin/python3

from flask import Blueprint

admin_views = Blueprint('admin_views', __name__, url_prefix='/admin')

from web_app.admin_views.brand_create_view import *
from web_app.admin_views.image_upload_view import *
from web_app.admin_views.phone_create_view import *
from web_app.admin_views.order_list_view import *
from web_app.admin_views.process_order_view import *
from web_app.admin_views.phone_list_view import *
from web_app.admin_views.ship_order_view import *
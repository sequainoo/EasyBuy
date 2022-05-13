from models.phone import Phone
from models.phone_brand import PhoneBrand
from models.image import Image
from models.customer import Customer
from models.address import Address
from models.region import Region
from models.city import City
from models.order import Order
from models.order_item import OrderItem
from models.payment import Payment
from models.account import Account
from models.base import Base

from models.storage_layer.storage import Storage

storage = Storage()
storage.reload()
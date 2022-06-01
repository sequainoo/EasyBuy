#!/usr/bin/python3
"""Module defines a storage layer on the sqlalchemy orm.

This layer interacts with the Session object for basic CRUD
on Models.
"""

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import (Base, Address, City, Region, Customer, Image, OrderItem,
                    Order, Payment, PhoneBrand, Phone, Account)

types = {'image': Image, 'order': Order,
         'address': Address, 'city': City,
         'phone': Phone, 'region': Region,
         'order-item': OrderItem, 'payment': Payment,
         'phone-brand': PhoneBrand, 'customer': Customer,
         'account': Account}


class Storage:
    """"""

    __engine = None
    __session = None

    def __init__(self):
        """"""
        connection_str = 'mysql+mysqldb://{}:{}@{}/{}'\
                          .format(getenv('EASYBUY_MYSQL_USER'),
                                 getenv('EASYBUY_MYSQL_PWD'),
                                 getenv('MYSQL_HOST'),
                                 getenv('EASYBUY_MYSQL_DB'))
        self.__engine = create_engine(connection_str)

    def reload(self):
        """Setups storage with new session object.
        Sets up the database if not setup"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=True)
        self.__session = Session()

    def all(self, model_type=''):
        """retrieves all objects of a particular type
        Precisely returns a query object,
        that must be iterated to retrieve the individual objects
        for efficiency.
        all results returned for a large data is not efficient for memory.

        Args:
            model_type (str): case insensitive model name, & '-' between 2 word names
        
        Return:
            Query object: that must be iterated for each obj for efficiency
        """
        if type(model_type) is not str:
            raise TypeError('model_type must be a string')

        Model = types.get(model_type.lower(), None)

        if not Model:
            raise ValueError('model_type must be a valid model type')

        return self.__session.query(Model)

    def get(self, model_type='', id_=''):
        """Get an object by type and id"""
        if type(id_) is not str:
            raise TypeError('id must be a string')
        if type(model_type) is not str:
            raise TypeError('model_type must be a string')

        Model = types.get(model_type.lower(), None)
        
        return self.__session.query(Model).get(id_)

    def add(self, obj):
        """adds an object to session"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Marks an object for deletion on the session"""
        if type(obj) not in types.values():
            raise TypeError('Incompatible Object type')
        self.__session.delete(obj)

    def count(self, model_type=''):
        """Returns the number of records for a specific Model"""
        if type(model_type) is not str:
            raise TypeError('model_type must be a string')
        Model = types.get(model_type, None)
        return self.__session.query(Model).count()

    def save(self):
        """commits the transaction session"""
        self.__session.commit()

    def rollback(self):
        """rollback session"""
        self.__session.rollback()

    def get_customer_by_email(self, email=''):
        """return a phone by email if exists or None"""
        if not email:
            raise ValueError('Provide email')
        if type(email) is not str:
            raise TypeError('email must be a string')
        query = self.__session.query(Customer).filter(Customer.email == email)
        return query.first()

    def get_orders_by_email(self, email=''):
        """Returns orders with a specific email"""
        if not email:
            return None
        customer_query = self.__session.query(Customer.id).filter(Customer.email == email)
        
        try:
            orders_query = self.__session.query(Order)\
                .filter(Order.customer_id == customer_query.scalar())
        except Exception:
            return None
        return orders_query

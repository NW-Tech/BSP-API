# coding: utf-8

"""
    IP RL BSP API

    IP RL BSP API for participation in capacity/energy market tenders.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NotificationReference(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'product_type': 'ProductType',
        'delivery_date': 'date',
        'market': 'ReserveMarket',
        'tender': 'TenderIdentification',
        'products': 'list[ProductName]'
    }

    attribute_map = {
        'product_type': 'productType',
        'delivery_date': 'deliveryDate',
        'market': 'market',
        'tender': 'tender',
        'products': 'products'
    }

    def __init__(self, product_type=None, delivery_date=None, market=None, tender=None, products=None):  # noqa: E501
        """NotificationReference - a model defined in Swagger"""  # noqa: E501
        self._product_type = None
        self._delivery_date = None
        self._market = None
        self._tender = None
        self._products = None
        self.discriminator = None
        if product_type is not None:
            self.product_type = product_type
        if delivery_date is not None:
            self.delivery_date = delivery_date
        if market is not None:
            self.market = market
        if tender is not None:
            self.tender = tender
        if products is not None:
            self.products = products

    @property
    def product_type(self):
        """Gets the product_type of this NotificationReference.  # noqa: E501


        :return: The product_type of this NotificationReference.  # noqa: E501
        :rtype: ProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this NotificationReference.


        :param product_type: The product_type of this NotificationReference.  # noqa: E501
        :type: ProductType
        """

        self._product_type = product_type

    @property
    def delivery_date(self):
        """Gets the delivery_date of this NotificationReference.  # noqa: E501

        Delivery day of offered control reserve / energy. (ISO 8601 format YYYY-MM-DD).  # noqa: E501

        :return: The delivery_date of this NotificationReference.  # noqa: E501
        :rtype: date
        """
        return self._delivery_date

    @delivery_date.setter
    def delivery_date(self, delivery_date):
        """Sets the delivery_date of this NotificationReference.

        Delivery day of offered control reserve / energy. (ISO 8601 format YYYY-MM-DD).  # noqa: E501

        :param delivery_date: The delivery_date of this NotificationReference.  # noqa: E501
        :type: date
        """

        self._delivery_date = delivery_date

    @property
    def market(self):
        """Gets the market of this NotificationReference.  # noqa: E501


        :return: The market of this NotificationReference.  # noqa: E501
        :rtype: ReserveMarket
        """
        return self._market

    @market.setter
    def market(self, market):
        """Sets the market of this NotificationReference.


        :param market: The market of this NotificationReference.  # noqa: E501
        :type: ReserveMarket
        """

        self._market = market

    @property
    def tender(self):
        """Gets the tender of this NotificationReference.  # noqa: E501


        :return: The tender of this NotificationReference.  # noqa: E501
        :rtype: TenderIdentification
        """
        return self._tender

    @tender.setter
    def tender(self, tender):
        """Sets the tender of this NotificationReference.


        :param tender: The tender of this NotificationReference.  # noqa: E501
        :type: TenderIdentification
        """

        self._tender = tender

    @property
    def products(self):
        """Gets the products of this NotificationReference.  # noqa: E501


        :return: The products of this NotificationReference.  # noqa: E501
        :rtype: list[ProductName]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this NotificationReference.


        :param products: The products of this NotificationReference.  # noqa: E501
        :type: list[ProductName]
        """

        self._products = products

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NotificationReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NotificationReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

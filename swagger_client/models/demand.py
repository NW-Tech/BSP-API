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

class Demand(object):
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
        'connecting_zone': 'ConnectingZone',
        'product_type': 'ProductType',
        'product_name': 'ProductName',
        'direction': 'Direction',
        'time_interval': 'TimeInterval',
        'data': 'DemandData'
    }

    attribute_map = {
        'connecting_zone': 'connectingZone',
        'product_type': 'productType',
        'product_name': 'productName',
        'direction': 'direction',
        'time_interval': 'timeInterval',
        'data': 'data'
    }

    def __init__(self, connecting_zone=None, product_type=None, product_name=None, direction=None, time_interval=None, data=None):  # noqa: E501
        """Demand - a model defined in Swagger"""  # noqa: E501
        self._connecting_zone = None
        self._product_type = None
        self._product_name = None
        self._direction = None
        self._time_interval = None
        self._data = None
        self.discriminator = None
        if connecting_zone is not None:
            self.connecting_zone = connecting_zone
        if product_type is not None:
            self.product_type = product_type
        if product_name is not None:
            self.product_name = product_name
        if direction is not None:
            self.direction = direction
        if time_interval is not None:
            self.time_interval = time_interval
        if data is not None:
            self.data = data

    @property
    def connecting_zone(self):
        """Gets the connecting_zone of this Demand.  # noqa: E501


        :return: The connecting_zone of this Demand.  # noqa: E501
        :rtype: ConnectingZone
        """
        return self._connecting_zone

    @connecting_zone.setter
    def connecting_zone(self, connecting_zone):
        """Sets the connecting_zone of this Demand.


        :param connecting_zone: The connecting_zone of this Demand.  # noqa: E501
        :type: ConnectingZone
        """

        self._connecting_zone = connecting_zone

    @property
    def product_type(self):
        """Gets the product_type of this Demand.  # noqa: E501


        :return: The product_type of this Demand.  # noqa: E501
        :rtype: ProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this Demand.


        :param product_type: The product_type of this Demand.  # noqa: E501
        :type: ProductType
        """

        self._product_type = product_type

    @property
    def product_name(self):
        """Gets the product_name of this Demand.  # noqa: E501


        :return: The product_name of this Demand.  # noqa: E501
        :rtype: ProductName
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this Demand.


        :param product_name: The product_name of this Demand.  # noqa: E501
        :type: ProductName
        """

        self._product_name = product_name

    @property
    def direction(self):
        """Gets the direction of this Demand.  # noqa: E501


        :return: The direction of this Demand.  # noqa: E501
        :rtype: Direction
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this Demand.


        :param direction: The direction of this Demand.  # noqa: E501
        :type: Direction
        """

        self._direction = direction

    @property
    def time_interval(self):
        """Gets the time_interval of this Demand.  # noqa: E501


        :return: The time_interval of this Demand.  # noqa: E501
        :rtype: TimeInterval
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this Demand.


        :param time_interval: The time_interval of this Demand.  # noqa: E501
        :type: TimeInterval
        """

        self._time_interval = time_interval

    @property
    def data(self):
        """Gets the data of this Demand.  # noqa: E501


        :return: The data of this Demand.  # noqa: E501
        :rtype: DemandData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Demand.


        :param data: The data of this Demand.  # noqa: E501
        :type: DemandData
        """

        self._data = data

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
        if issubclass(Demand, dict):
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
        if not isinstance(other, Demand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
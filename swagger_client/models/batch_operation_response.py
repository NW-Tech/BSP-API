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

class BatchOperationResponse(object):
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
        'status': 'int',
        'headers': 'dict(str, str)',
        'body': 'object'
    }

    attribute_map = {
        'status': 'status',
        'headers': 'headers',
        'body': 'body'
    }

    def __init__(self, status=None, headers=None, body=None):  # noqa: E501
        """BatchOperationResponse - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._headers = None
        self._body = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if headers is not None:
            self.headers = headers
        if body is not None:
            self.body = body

    @property
    def status(self):
        """Gets the status of this BatchOperationResponse.  # noqa: E501

        HTTP status code.  # noqa: E501

        :return: The status of this BatchOperationResponse.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchOperationResponse.

        HTTP status code.  # noqa: E501

        :param status: The status of this BatchOperationResponse.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def headers(self):
        """Gets the headers of this BatchOperationResponse.  # noqa: E501

        HTTP response header.  # noqa: E501

        :return: The headers of this BatchOperationResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this BatchOperationResponse.

        HTTP response header.  # noqa: E501

        :param headers: The headers of this BatchOperationResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def body(self):
        """Gets the body of this BatchOperationResponse.  # noqa: E501


        :return: The body of this BatchOperationResponse.  # noqa: E501
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchOperationResponse.


        :param body: The body of this BatchOperationResponse.  # noqa: E501
        :type: object
        """

        self._body = body

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
        if issubclass(BatchOperationResponse, dict):
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
        if not isinstance(other, BatchOperationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

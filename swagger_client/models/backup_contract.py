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

class BackupContract(object):
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
        'id': 'ResourceIdentification',
        'product_type': 'ProductType',
        'backup_provider': 'BalancingServiceProvider',
        'backed_up_provider': 'BalancingServiceProvider',
        'validity_period': 'ContractValidityPeriod'
    }

    attribute_map = {
        'id': 'id',
        'product_type': 'productType',
        'backup_provider': 'backupProvider',
        'backed_up_provider': 'backedUpProvider',
        'validity_period': 'validityPeriod'
    }

    def __init__(self, id=None, product_type=None, backup_provider=None, backed_up_provider=None, validity_period=None):  # noqa: E501
        """BackupContract - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._product_type = None
        self._backup_provider = None
        self._backed_up_provider = None
        self._validity_period = None
        self.discriminator = None
        self.id = id
        if product_type is not None:
            self.product_type = product_type
        if backup_provider is not None:
            self.backup_provider = backup_provider
        if backed_up_provider is not None:
            self.backed_up_provider = backed_up_provider
        if validity_period is not None:
            self.validity_period = validity_period

    @property
    def id(self):
        """Gets the id of this BackupContract.  # noqa: E501


        :return: The id of this BackupContract.  # noqa: E501
        :rtype: ResourceIdentification
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupContract.


        :param id: The id of this BackupContract.  # noqa: E501
        :type: ResourceIdentification
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def product_type(self):
        """Gets the product_type of this BackupContract.  # noqa: E501


        :return: The product_type of this BackupContract.  # noqa: E501
        :rtype: ProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this BackupContract.


        :param product_type: The product_type of this BackupContract.  # noqa: E501
        :type: ProductType
        """

        self._product_type = product_type

    @property
    def backup_provider(self):
        """Gets the backup_provider of this BackupContract.  # noqa: E501


        :return: The backup_provider of this BackupContract.  # noqa: E501
        :rtype: BalancingServiceProvider
        """
        return self._backup_provider

    @backup_provider.setter
    def backup_provider(self, backup_provider):
        """Sets the backup_provider of this BackupContract.


        :param backup_provider: The backup_provider of this BackupContract.  # noqa: E501
        :type: BalancingServiceProvider
        """

        self._backup_provider = backup_provider

    @property
    def backed_up_provider(self):
        """Gets the backed_up_provider of this BackupContract.  # noqa: E501


        :return: The backed_up_provider of this BackupContract.  # noqa: E501
        :rtype: BalancingServiceProvider
        """
        return self._backed_up_provider

    @backed_up_provider.setter
    def backed_up_provider(self, backed_up_provider):
        """Sets the backed_up_provider of this BackupContract.


        :param backed_up_provider: The backed_up_provider of this BackupContract.  # noqa: E501
        :type: BalancingServiceProvider
        """

        self._backed_up_provider = backed_up_provider

    @property
    def validity_period(self):
        """Gets the validity_period of this BackupContract.  # noqa: E501


        :return: The validity_period of this BackupContract.  # noqa: E501
        :rtype: ContractValidityPeriod
        """
        return self._validity_period

    @validity_period.setter
    def validity_period(self, validity_period):
        """Sets the validity_period of this BackupContract.


        :param validity_period: The validity_period of this BackupContract.  # noqa: E501
        :type: ContractValidityPeriod
        """

        self._validity_period = validity_period

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
        if issubclass(BackupContract, dict):
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
        if not isinstance(other, BackupContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
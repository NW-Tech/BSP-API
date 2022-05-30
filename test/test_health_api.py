# coding: utf-8

"""
    IP RL BSP API

    IP RL BSP API for participation in capacity/energy market tenders.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.health_api import HealthApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_health_informations(self):
        """Test case for get_api_health_informations

        API health endpoint.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

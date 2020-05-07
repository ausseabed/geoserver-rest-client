# coding: utf-8

"""
    GeoServer System Status

    Request provides details about OWS and REST requests that GeoServer has handled  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_system-status
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_system-status.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_monitor_requests(self):
        """Test case for get_monitor_requests

        Get a list of requests  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
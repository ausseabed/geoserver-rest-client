# coding: utf-8

"""
    GeoWebCache Index

    The front facing html ui for GeoWebCache.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_gwcindex
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_gwcindex.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_index_get(self):
        """Test case for index_get

        Returns the HTML user interface  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

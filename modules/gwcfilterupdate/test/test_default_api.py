# coding: utf-8

"""
    GeoWebCache Filter Update

    The REST API for Updating GWC filter  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_gwcfilterupdate
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_gwcfilterupdate.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_filter_update_post(self):
        """Test case for filter_update_post

        Updates a given layer filter by way of xml or zip file.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

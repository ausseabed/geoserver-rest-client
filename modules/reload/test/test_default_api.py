# coding: utf-8

"""
    GeoServer Reset/Reload

    Reset/Reload clears internal caches and reloads configuation from disk  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_reload
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_reload.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_reload(self):
        """Test case for delete_reload

        """
        pass

    def test_delete_reset(self):
        """Test case for delete_reset

        """
        pass

    def test_get_reload(self):
        """Test case for get_reload

        """
        pass

    def test_get_reset(self):
        """Test case for get_reset

        """
        pass

    def test_post_reload(self):
        """Test case for post_reload

        Reload the configuration from disk, and reset all caches.  # noqa: E501
        """
        pass

    def test_post_reset(self):
        """Test case for post_reset

        Reset all store, raster, and schema caches.  # noqa: E501
        """
        pass

    def test_put_reload(self):
        """Test case for put_reload

        Reload the configuration from disk, and reset all caches.  # noqa: E501
        """
        pass

    def test_put_reset(self):
        """Test case for put_reset

        Reset all store, raster, and schema caches.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

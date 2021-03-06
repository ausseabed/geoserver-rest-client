# coding: utf-8

"""
    GeoWebCache GridSets

    A Grid Set is a set of tile grids associated with a coordinate reference system.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_gwcgridsets
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_gwcgridsets.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_gridset_delete(self):
        """Test case for gridset_delete

        Delete configured gridset  # noqa: E501
        """
        pass

    def test_gridset_get(self):
        """Test case for gridset_get

        Retrieve a configured gridset  # noqa: E501
        """
        pass

    def test_gridset_put(self):
        """Test case for gridset_put

        Create or update a configured gridset.  # noqa: E501
        """
        pass

    def test_gridsets_get(self):
        """Test case for gridsets_get

        Get a list of configured gridsets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

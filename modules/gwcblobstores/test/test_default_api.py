# coding: utf-8

"""
    GeoWebCache Blobstores

    BlobStores configure the persistance of tile data.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_gwcblobstores
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_gwcblobstores.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_blobstore_delete(self):
        """Test case for blobstore_delete

        Delete configured blobstore  # noqa: E501
        """
        pass

    def test_blobstore_get(self):
        """Test case for blobstore_get

        Retrieve a configured blobstore  # noqa: E501
        """
        pass

    def test_blobstore_put(self):
        """Test case for blobstore_put

        Create or update a configured blobstore.  # noqa: E501
        """
        pass

    def test_blobstores_get(self):
        """Test case for blobstores_get

        Get a list of configured blobstores  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

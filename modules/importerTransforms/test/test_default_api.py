# coding: utf-8

"""
    GeoServer Importer Extension - Transforms

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The transforms endpoint manages data transforms applied to sindividual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_importerTransforms
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_importerTransforms.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_transform(self):
        """Test case for delete_transform

        Removes the transformation  # noqa: E501
        """
        pass

    def test_get_transform(self):
        """Test case for get_transform

        Retrieve a transformation  # noqa: E501
        """
        pass

    def test_get_transforms(self):
        """Test case for get_transforms

        Retrieve transformation list  # noqa: E501
        """
        pass

    def test_post_transform(self):
        """Test case for post_transform

        Create a new transformation  # noqa: E501
        """
        pass

    def test_put_transform(self):
        """Test case for put_transform

        Modifies a transformation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    GeoServer Importer Extension - Main

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The main endpoint manages individual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_importer
from model.attributes_to_point_geometry_transform import AttributesToPointGeometryTransform  # noqa: E501
from gs_rest_api_importer.rest import ApiException


class TestAttributesToPointGeometryTransform(unittest.TestCase):
    """AttributesToPointGeometryTransform unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttributesToPointGeometryTransform(self):
        """Test AttributesToPointGeometryTransform"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gs_rest_api_importer.models.attributes_to_point_geometry_transform.AttributesToPointGeometryTransform()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

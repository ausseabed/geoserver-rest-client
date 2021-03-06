# coding: utf-8

"""
    GeoServer Manifests API

    GeoServer provides a REST service to expose a listing of all loaded JARs and resources on the running instance. This is useful for bug reports and to keep track of extensions deployed into the application.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_manifests
from model.manifest import Manifest  # noqa: E501
from gs_rest_api_manifests.rest import ApiException


class TestManifest(unittest.TestCase):
    """Manifest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testManifest(self):
        """Test Manifest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gs_rest_api_manifests.models.manifest.Manifest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

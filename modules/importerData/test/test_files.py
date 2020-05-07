# coding: utf-8

"""
    GeoServer Importer Extension - Data

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The data endpoint controls uploading layer data to specific import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_importerData
from model.files import Files  # noqa: E501
from gs_rest_api_importerData.rest import ApiException


class TestFiles(unittest.TestCase):
    """Files unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFiles(self):
        """Test Files"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gs_rest_api_importerData.models.files.Files()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

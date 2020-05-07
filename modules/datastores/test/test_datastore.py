# coding: utf-8

"""
    GeoServer Data Stores

    A data store contains vector format spatial data. It can be a file (such as a shapefile), a database (such as PostGIS), or a server (such as a remote Web Feature Service).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_datastores
from model.datastore import Datastore  # noqa: E501
from gs_rest_api_datastores.rest import ApiException


class TestDatastore(unittest.TestCase):
    """Datastore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatastore(self):
        """Test Datastore"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gs_rest_api_datastores.models.datastore.Datastore()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
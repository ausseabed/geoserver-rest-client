# coding: utf-8

"""
    GeoServer Data Stores

    A data store contains vector format spatial data. It can be a file (such as a shapefile), a database (such as PostGIS), or a server (such as a remote Web Feature Service).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gs_rest_api_datastores
from gs_rest_api_datastores.model.entry import Entry  # noqa: E501
from gs_rest_api_datastores.rest import ApiException

class TestEntry(unittest.TestCase):
    """Entry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Entry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gs_rest_api_datastores.models.entry.Entry()  # noqa: E501
        if include_optional :
            return Entry(
                key = '0', 
                value = '0'
            )
        else :
            return Entry(
        )

    def testEntry(self):
        """Test Entry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

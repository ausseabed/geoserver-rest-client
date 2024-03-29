# coding: utf-8

"""
    GeoServer Feature Types

    A feature type is a vector based spatial resource or data set that originates from a data store. In some cases, such as with a shapefile, a feature type has a one-to-one relationship with its data store. In other cases, such as PostGIS, the relationship of feature type to data store is many-to-one, feature types corresponding to a table in the database.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_featuretypes
from model.feature_type_info_wrapper import FeatureTypeInfoWrapper  # noqa: E501
from gs_rest_api_featuretypes.rest import ApiException


class TestFeatureTypeInfoWrapper(unittest.TestCase):
    """FeatureTypeInfoWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFeatureTypeInfoWrapper(self):
        """Test FeatureTypeInfoWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = gs_rest_api_featuretypes.models.feature_type_info_wrapper.FeatureTypeInfoWrapper()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

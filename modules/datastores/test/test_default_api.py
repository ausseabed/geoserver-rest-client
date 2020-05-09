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
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_datastores.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clean_all_mongo_schemas(self):
        """Test case for clean_all_mongo_schemas

        Cleans all MongoDB internal stores Schemas for an App-Schema store.  # noqa: E501
        """
        pass

    def test_clean_mongo_schema(self):
        """Test case for clean_mongo_schema

        Cleans a MongoDB internal store Schemas for an App-Schema store.  # noqa: E501
        """
        pass

    def test_delete_datastore(self):
        """Test case for delete_datastore

        Delete data store  # noqa: E501
        """
        pass

    def test_get_data_store(self):
        """Test case for get_data_store

        Retrieve a particular data store from a workspace  # noqa: E501
        """
        pass

    def test_get_data_store_upload(self):
        """Test case for get_data_store_upload

        """
        pass

    def test_get_datastores(self):
        """Test case for get_datastores

        Get a list of data stores  # noqa: E501
        """
        pass

    def test_post_datastores(self):
        """Test case for post_datastores

        Create a new data store  # noqa: E501
        """
        pass

    def test_put_data_store_upload(self):
        """Test case for put_data_store_upload

        Uploads files to the data store, creating it if necessary  # noqa: E501
        """
        pass

    def test_put_datastore(self):
        """Test case for put_datastore

        Modify a data store.  # noqa: E501
        """
        pass

    def test_rebuild_all_mongo_schemas(self):
        """Test case for rebuild_all_mongo_schemas

        Rebuilds all MongoDB internal stores Schemas for an App-Schema store.  # noqa: E501
        """
        pass

    def test_rebuild_mongo_schema(self):
        """Test case for rebuild_mongo_schema

        Rebuilds a MongoDB internal store Schemas for an App-Schema store.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

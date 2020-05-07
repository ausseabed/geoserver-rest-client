# coding: utf-8

"""
    GeoServer Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_layers
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_layers.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_layers_delete(self):
        """Test case for layers_delete

        """
        pass

    def test_layers_get(self):
        """Test case for layers_get

        Get a list of layers  # noqa: E501
        """
        pass

    def test_layers_name_delete(self):
        """Test case for layers_name_delete

        Delete layer  # noqa: E501
        """
        pass

    def test_layers_name_get(self):
        """Test case for layers_name_get

        Retrieve a layer  # noqa: E501
        """
        pass

    def test_layers_name_post(self):
        """Test case for layers_name_post

        """
        pass

    def test_layers_name_put(self):
        """Test case for layers_name_put

        Modify a layer.  # noqa: E501
        """
        pass

    def test_layers_name_workspace_delete(self):
        """Test case for layers_name_workspace_delete

        Delete layer  # noqa: E501
        """
        pass

    def test_layers_name_workspace_get(self):
        """Test case for layers_name_workspace_get

        Retrieve a layer  # noqa: E501
        """
        pass

    def test_layers_name_workspace_post(self):
        """Test case for layers_name_workspace_post

        """
        pass

    def test_layers_name_workspace_put(self):
        """Test case for layers_name_workspace_put

        Modify a layer.  # noqa: E501
        """
        pass

    def test_layers_post(self):
        """Test case for layers_post

        """
        pass

    def test_layers_put(self):
        """Test case for layers_put

        """
        pass

    def test_layers_workspace_delete(self):
        """Test case for layers_workspace_delete

        """
        pass

    def test_layers_workspace_get(self):
        """Test case for layers_workspace_get

        Get a list of layers in a workspace.  # noqa: E501
        """
        pass

    def test_layers_workspace_post(self):
        """Test case for layers_workspace_post

        """
        pass

    def test_layers_workspace_put(self):
        """Test case for layers_workspace_put

        """
        pass


if __name__ == '__main__':
    unittest.main()

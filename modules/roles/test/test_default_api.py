# coding: utf-8

"""
    Roles

    Organisation of security roles  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import gs_rest_api_roles
from api.default_api import DefaultApi  # noqa: E501
from gs_rest_api_roles.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_role_default_delete(self):
        """Test case for role_default_delete

        Delete a role  # noqa: E501
        """
        pass

    def test_role_default_group_delete(self):
        """Test case for role_default_group_delete

        Disassociate a role from a group  # noqa: E501
        """
        pass

    def test_role_default_group_post(self):
        """Test case for role_default_group_post

        Associate a role with a group  # noqa: E501
        """
        pass

    def test_role_default_post(self):
        """Test case for role_default_post

        Add a role  # noqa: E501
        """
        pass

    def test_role_default_user_delete(self):
        """Test case for role_default_user_delete

        Disassociate a role from a user  # noqa: E501
        """
        pass

    def test_role_default_user_post(self):
        """Test case for role_default_user_post

        Associate a role with a user  # noqa: E501
        """
        pass

    def test_role_delete(self):
        """Test case for role_delete

        Delete a role  # noqa: E501
        """
        pass

    def test_role_group_delete(self):
        """Test case for role_group_delete

        Disassociate a role from a group  # noqa: E501
        """
        pass

    def test_role_group_post(self):
        """Test case for role_group_post

        Associate a role with a group  # noqa: E501
        """
        pass

    def test_role_post(self):
        """Test case for role_post

        Add a role  # noqa: E501
        """
        pass

    def test_role_user_delete(self):
        """Test case for role_user_delete

        Disassociate a role from a user  # noqa: E501
        """
        pass

    def test_role_user_post(self):
        """Test case for role_user_post

        Associate a role with a user  # noqa: E501
        """
        pass

    def test_roles_default_get(self):
        """Test case for roles_default_get

        Query all roles  # noqa: E501
        """
        pass

    def test_roles_default_group_get(self):
        """Test case for roles_default_group_get

        Query all roles for group  # noqa: E501
        """
        pass

    def test_roles_default_user_get(self):
        """Test case for roles_default_user_get

        Query all roles for user  # noqa: E501
        """
        pass

    def test_roles_get(self):
        """Test case for roles_get

        Query all roles  # noqa: E501
        """
        pass

    def test_roles_group_get(self):
        """Test case for roles_group_get

        Query all roles for group  # noqa: E501
        """
        pass

    def test_roles_user_get(self):
        """Test case for roles_user_get

        Query all roles for user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

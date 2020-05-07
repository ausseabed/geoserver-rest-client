# coding: utf-8

"""
    GeoWebCache GridSets

    A Grid Set is a set of tile grids associated with a coordinate reference system.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gs_rest_api_gwcgridsets.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def gridset_delete(self, gridset_name, **kwargs):  # noqa: E501
        """Delete configured gridset  # noqa: E501

        Deletes a configured gridset from the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_delete(gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gridset_name: The name of the gridset to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gridset_delete_with_http_info(gridset_name, **kwargs)  # noqa: E501
        else:
            (data) = self.gridset_delete_with_http_info(gridset_name, **kwargs)  # noqa: E501
            return data

    def gridset_delete_with_http_info(self, gridset_name, **kwargs):  # noqa: E501
        """Delete configured gridset  # noqa: E501

        Deletes a configured gridset from the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_delete_with_http_info(gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gridset_name: The name of the gridset to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gridset_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gridset_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gridset_name' is set
        if ('gridset_name' not in params or
                params['gridset_name'] is None):
            raise ValueError("Missing the required parameter `gridset_name` when calling `gridset_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gridset_name' in params:
            path_params['gridsetName'] = params['gridset_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/gridsets/{gridsetName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gridset_get(self, gridset_name, **kwargs):  # noqa: E501
        """Retrieve a configured gridset  # noqa: E501

        Retrieves a single configured gridset definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_get(gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gridset_name: The name of the gridset to retrieve. (required)
        :return: GridSet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gridset_get_with_http_info(gridset_name, **kwargs)  # noqa: E501
        else:
            (data) = self.gridset_get_with_http_info(gridset_name, **kwargs)  # noqa: E501
            return data

    def gridset_get_with_http_info(self, gridset_name, **kwargs):  # noqa: E501
        """Retrieve a configured gridset  # noqa: E501

        Retrieves a single configured gridset definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_get_with_http_info(gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gridset_name: The name of the gridset to retrieve. (required)
        :return: GridSet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gridset_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gridset_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gridset_name' is set
        if ('gridset_name' not in params or
                params['gridset_name'] is None):
            raise ValueError("Missing the required parameter `gridset_name` when calling `gridset_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gridset_name' in params:
            path_params['gridsetName'] = params['gridset_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/gridsets/{gridsetName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GridSet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gridset_put(self, body, gridset_name, **kwargs):  # noqa: E501
        """Create or update a configured gridset.  # noqa: E501

        Creates a new configured gridset on the server, or modifies an existing gridset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_put(body, gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GridSet body: The new gridset definition. (required)
        :param str gridset_name: The name of the gridset to add or update. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gridset_put_with_http_info(body, gridset_name, **kwargs)  # noqa: E501
        else:
            (data) = self.gridset_put_with_http_info(body, gridset_name, **kwargs)  # noqa: E501
            return data

    def gridset_put_with_http_info(self, body, gridset_name, **kwargs):  # noqa: E501
        """Create or update a configured gridset.  # noqa: E501

        Creates a new configured gridset on the server, or modifies an existing gridset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridset_put_with_http_info(body, gridset_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GridSet body: The new gridset definition. (required)
        :param str gridset_name: The name of the gridset to add or update. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'gridset_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gridset_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `gridset_put`")  # noqa: E501
        # verify the required parameter 'gridset_name' is set
        if ('gridset_name' not in params or
                params['gridset_name'] is None):
            raise ValueError("Missing the required parameter `gridset_name` when calling `gridset_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gridset_name' in params:
            path_params['gridsetName'] = params['gridset_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/gridsets/{gridsetName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def gridsets_get(self, **kwargs):  # noqa: E501
        """Get a list of configured gridsets  # noqa: E501

        Displays a list of all configured gridsets on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridsets_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GridSets
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.gridsets_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.gridsets_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def gridsets_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of configured gridsets  # noqa: E501

        Displays a list of all configured gridsets on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gridsets_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GridSets
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gridsets_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/gridsets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GridSets',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

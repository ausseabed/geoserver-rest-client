# coding: utf-8

"""
    GeoServer Importer Extension - Main

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The main endpoint manages individual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gs_rest_api_importer.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_import(self, **kwargs):  # noqa: E501
        """Delete an import  # noqa: E501

        Deletes the import with id {importId}, as long as it is not in the COMPLETE state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_import(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_import_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_import_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_import_with_http_info(self, **kwargs):  # noqa: E501
        """Delete an import  # noqa: E501

        Deletes the import with id {importId}, as long as it is not in the COMPLETE state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_import_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method delete_import" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports/{importId}', 'DELETE',
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

    def delete_imports(self, **kwargs):  # noqa: E501
        """Delete all imports  # noqa: E501

        Deletes all imports that are not in the COMPLETE state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_imports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_imports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_imports_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_imports_with_http_info(self, **kwargs):  # noqa: E501
        """Delete all imports  # noqa: E501

        Deletes all imports that are not in the COMPLETE state.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_imports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
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
                    " to method delete_imports" % key
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
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports', 'DELETE',
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

    def get_import(self, import_id, **kwargs):  # noqa: E501
        """Retrieve import by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_import(import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str import_id: The ID of the import (required)
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_import_with_http_info(import_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_import_with_http_info(import_id, **kwargs)  # noqa: E501
            return data

    def get_import_with_http_info(self, import_id, **kwargs):  # noqa: E501
        """Retrieve import by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_import_with_http_info(import_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str import_id: The ID of the import (required)
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['import_id', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params or
                params['import_id'] is None):
            raise ValueError("Missing the required parameter `import_id` when calling `get_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'import_id' in params:
            path_params['importId'] = params['import_id']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/html', 'application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports/{importId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Context',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_imports(self, **kwargs):  # noqa: E501
        """Get a list of all imports  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_imports(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Contexts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_imports_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_imports_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_imports_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of all imports  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_imports_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Contexts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_imports" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contexts',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_import(self, body, **kwargs):  # noqa: E501
        """Create a new import, or execute an existing import  # noqa: E501

        If an import with the id {importId} exists and is not in the INIT state, it is executed. If an import with that id does not exist, a new import is created with that id. If the exec parameter is true, this new import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_import(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_import_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_import_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_import_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new import, or execute an existing import  # noqa: E501

        If an import with the id {importId} exists and is not in the INIT state, it is executed. If an import with that id does not exist, a new import is created with that id. If the exec parameter is true, this new import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_import_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', '_async', '_exec', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_async' in params:
            query_params.append(('async', params['_async']))  # noqa: E501
        if '_exec' in params:
            query_params.append(('exec', params['_exec']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports/{importId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Context',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_imports(self, body, **kwargs):  # noqa: E501
        """Create a new import  # noqa: E501

        Creates a new import. If the exec parameter is true, that import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_imports(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_imports_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_imports_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_imports_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a new import  # noqa: E501

        Creates a new import. If the exec parameter is true, that import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_imports_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', '_async', '_exec', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_imports" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_imports`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_async' in params:
            query_params.append(('async', params['_async']))  # noqa: E501
        if '_exec' in params:
            query_params.append(('exec', params['_exec']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Context',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_import(self, body, **kwargs):  # noqa: E501
        """Tries to create a new import with the provided id.  # noqa: E501

        Creates a new import with the next unclaimed id >= {importId}. If the exec parameter is true, that import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_import(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_import_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_import_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_import_with_http_info(self, body, **kwargs):  # noqa: E501
        """Tries to create a new import with the provided id.  # noqa: E501

        Creates a new import with the next unclaimed id >= {importId}. If the exec parameter is true, that import is immediately executed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_import_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Context body: The import context to create. (required)
        :param bool _async: Run the import asyncronously.
        :param bool _exec: Run the import when it is created.
        :param str expand: What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to.
        :return: Context
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', '_async', '_exec', 'expand']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_async' in params:
            query_params.append(('async', params['_async']))  # noqa: E501
        if '_exec' in params:
            query_params.append(('exec', params['_exec']))  # noqa: E501
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/imports/{importId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Context',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

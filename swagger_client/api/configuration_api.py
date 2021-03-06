# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 9.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ConfigurationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def configuration_controller_create_directory(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Create a configuration directory.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_create_directory(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body16 body: The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the directory. (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_create_directory_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_create_directory_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
            return data

    def configuration_controller_create_directory_with_http_info(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Create a configuration directory.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_create_directory_with_http_info(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body16 body: The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the directory. (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api', 'user_agent', 'instance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_create_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `configuration_controller_create_directory`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_create_directory`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_create_directory`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_create_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigurationFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def configuration_controller_delete_directory(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Deletes an empty directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_delete_directory(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body24 body: A Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the path to the directory to delete (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_delete_directory_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_delete_directory_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
            return data

    def configuration_controller_delete_directory_with_http_info(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Deletes an empty directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_delete_directory_with_http_info(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body24 body: A Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the path to the directory to delete (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api', 'user_agent', 'instance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_delete_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `configuration_controller_delete_directory`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_delete_directory`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_delete_directory`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_delete_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config', 'DELETE',
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

    def configuration_controller_directory(self, api, user_agent, instance, directory_path, **kwargs):  # noqa: E501
        """Get the contents of a directory at a directoryPath  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_directory(api, user_agent, instance, directory_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param str directory_path: The path of the directory to get (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_directory_with_http_info(api, user_agent, instance, directory_path, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_directory_with_http_info(api, user_agent, instance, directory_path, **kwargs)  # noqa: E501
            return data

    def configuration_controller_directory_with_http_info(self, api, user_agent, instance, directory_path, **kwargs):  # noqa: E501
        """Get the contents of a directory at a directoryPath  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_directory_with_http_info(api, user_agent, instance, directory_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param str directory_path: The path of the directory to get (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'instance', 'directory_path', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_directory" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_directory`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_directory`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_directory`")  # noqa: E501
        # verify the required parameter 'directory_path' is set
        if ('directory_path' not in params or
                params['directory_path'] is None):
            raise ValueError("Missing the required parameter `directory_path` when calling `configuration_controller_directory`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'directory_path' in params:
            path_params['directoryPath'] = params['directory_path']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config/List/{directoryPath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedConfigurationFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def configuration_controller_file(self, api, user_agent, instance, file_path, **kwargs):  # noqa: E501
        """Get the contents of a file at a filePath  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_file(api, user_agent, instance, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param str file_path: The path of the file to get (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_file_with_http_info(api, user_agent, instance, file_path, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_file_with_http_info(api, user_agent, instance, file_path, **kwargs)  # noqa: E501
            return data

    def configuration_controller_file_with_http_info(self, api, user_agent, instance, file_path, **kwargs):  # noqa: E501
        """Get the contents of a file at a filePath  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_file_with_http_info(api, user_agent, instance, file_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param str file_path: The path of the file to get (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'instance', 'file_path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_file`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_file`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_file`")  # noqa: E501
        # verify the required parameter 'file_path' is set
        if ('file_path' not in params or
                params['file_path'] is None):
            raise ValueError("Missing the required parameter `file_path` when calling `configuration_controller_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'file_path' in params:
            path_params['filePath'] = params['file_path']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config/File/{filePath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigurationFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def configuration_controller_list(self, api, user_agent, instance, **kwargs):  # noqa: E501
        """Get the contents of the root configuration directory.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_list(api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_list_with_http_info(api, user_agent, instance, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_list_with_http_info(api, user_agent, instance, **kwargs)  # noqa: E501
            return data

    def configuration_controller_list_with_http_info(self, api, user_agent, instance, **kwargs):  # noqa: E501
        """Get the contents of the root configuration directory.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_list_with_http_info(api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'instance', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_list`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_list`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config/List', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedConfigurationFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def configuration_controller_update(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Write to a configuration file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_update(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body20 body: The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the file. (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configuration_controller_update_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
        else:
            (data) = self.configuration_controller_update_with_http_info(body, api, user_agent, instance, **kwargs)  # noqa: E501
            return data

    def configuration_controller_update_with_http_info(self, body, api, user_agent, instance, **kwargs):  # noqa: E501
        """Write to a configuration file.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configuration_controller_update_with_http_info(body, api, user_agent, instance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Body20 body: The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the file. (required)
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int instance: The instance ID being accessed (required)
        :return: ConfigurationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'api', 'user_agent', 'instance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configuration_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `configuration_controller_update`")  # noqa: E501
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `configuration_controller_update`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `configuration_controller_update`")  # noqa: E501
        # verify the required parameter 'instance' is set
        if ('instance' not in params or
                params['instance'] is None):
            raise ValueError("Missing the required parameter `instance` when calling `configuration_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501
        if 'instance' in params:
            header_params['Instance'] = params['instance']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Config', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ConfigurationFileResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 8.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class UserGroupApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def user_group_controller_create(self, api, user_agent, **kwargs):  # noqa: E501
        """Create a new Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_create(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Body68 body: The Tgstation.Server.Api.Models.UserGroup to create.
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_group_controller_create_with_http_info(api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.user_group_controller_create_with_http_info(api, user_agent, **kwargs)  # noqa: E501
            return data

    def user_group_controller_create_with_http_info(self, api, user_agent, **kwargs):  # noqa: E501
        """Create a new Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_create_with_http_info(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Body68 body: The Tgstation.Server.Api.Models.UserGroup to create.
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_group_controller_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `user_group_controller_create`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `user_group_controller_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

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
            '/UserGroup', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_group_controller_delete(self, api, user_agent, id, **kwargs):  # noqa: E501
        """Delete an Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_delete(api, user_agent, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int id: The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_group_controller_delete_with_http_info(api, user_agent, id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_group_controller_delete_with_http_info(api, user_agent, id, **kwargs)  # noqa: E501
            return data

    def user_group_controller_delete_with_http_info(self, api, user_agent, id, **kwargs):  # noqa: E501
        """Delete an Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_delete_with_http_info(api, user_agent, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int id: The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_group_controller_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `user_group_controller_delete`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `user_group_controller_delete`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_group_controller_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/UserGroup/{id}', 'DELETE',
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

    def user_group_controller_get_id(self, api, user_agent, id, **kwargs):  # noqa: E501
        """Gets a specific Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_get_id(api, user_agent, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int id: The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup. (required)
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_group_controller_get_id_with_http_info(api, user_agent, id, **kwargs)  # noqa: E501
        else:
            (data) = self.user_group_controller_get_id_with_http_info(api, user_agent, id, **kwargs)  # noqa: E501
            return data

    def user_group_controller_get_id_with_http_info(self, api, user_agent, id, **kwargs):  # noqa: E501
        """Gets a specific Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_get_id_with_http_info(api, user_agent, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int id: The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup. (required)
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_group_controller_get_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `user_group_controller_get_id`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `user_group_controller_get_id`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `user_group_controller_get_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/UserGroup/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_group_controller_list(self, api, user_agent, **kwargs):  # noqa: E501
        """Lists all Tgstation.Server.Api.Models.UserGroups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_list(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedUserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_group_controller_list_with_http_info(api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.user_group_controller_list_with_http_info(api, user_agent, **kwargs)  # noqa: E501
            return data

    def user_group_controller_list_with_http_info(self, api, user_agent, **kwargs):  # noqa: E501
        """Lists all Tgstation.Server.Api.Models.UserGroups.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_list_with_http_info(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param int page: The current page.
        :param int page_size: The page size.
        :return: PaginatedUserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_group_controller_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `user_group_controller_list`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `user_group_controller_list`")  # noqa: E501

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

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/UserGroup/List', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedUserGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def user_group_controller_update(self, api, user_agent, **kwargs):  # noqa: E501
        """Update a Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_update(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Body72 body: The Tgstation.Server.Api.Models.UserGroup to update.
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.user_group_controller_update_with_http_info(api, user_agent, **kwargs)  # noqa: E501
        else:
            (data) = self.user_group_controller_update_with_http_info(api, user_agent, **kwargs)  # noqa: E501
            return data

    def user_group_controller_update_with_http_info(self, api, user_agent, **kwargs):  # noqa: E501
        """Update a Tgstation.Server.Api.Models.UserGroup.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.user_group_controller_update_with_http_info(api, user_agent, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param Body72 body: The Tgstation.Server.Api.Models.UserGroup to update.
        :return: UserGroup
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method user_group_controller_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `user_group_controller_update`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `user_group_controller_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'api' in params:
            header_params['Api'] = params['api']  # noqa: E501
        if 'user_agent' in params:
            header_params['User-Agent'] = params['user_agent']  # noqa: E501

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
            '/UserGroup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserGroup',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
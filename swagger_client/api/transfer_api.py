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


class TransferApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transfer_controller_download(self, api, user_agent, ticket, **kwargs):  # noqa: E501
        """Downloads a file with a given ticket.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_controller_download(api, user_agent, ticket, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param str ticket: The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the download. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transfer_controller_download_with_http_info(api, user_agent, ticket, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_controller_download_with_http_info(api, user_agent, ticket, **kwargs)  # noqa: E501
            return data

    def transfer_controller_download_with_http_info(self, api, user_agent, ticket, **kwargs):  # noqa: E501
        """Downloads a file with a given ticket.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_controller_download_with_http_info(api, user_agent, ticket, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param str ticket: The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the download. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'ticket']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_controller_download" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `transfer_controller_download`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `transfer_controller_download`")  # noqa: E501
        # verify the required parameter 'ticket' is set
        if ('ticket' not in params or
                params['ticket'] is None):
            raise ValueError("Missing the required parameter `ticket` when calling `transfer_controller_download`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ticket' in params:
            query_params.append(('ticket', params['ticket']))  # noqa: E501

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
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Transfer', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def transfer_controller_upload(self, api, user_agent, ticket, **kwargs):  # noqa: E501
        """Uploads a file with a given ticket.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_controller_upload(api, user_agent, ticket, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param str ticket: The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the upload. (required)
        :param Object body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transfer_controller_upload_with_http_info(api, user_agent, ticket, **kwargs)  # noqa: E501
        else:
            (data) = self.transfer_controller_upload_with_http_info(api, user_agent, ticket, **kwargs)  # noqa: E501
            return data

    def transfer_controller_upload_with_http_info(self, api, user_agent, ticket, **kwargs):  # noqa: E501
        """Uploads a file with a given ticket.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transfer_controller_upload_with_http_info(api, user_agent, ticket, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api: The API version being used in the form \"Tgstation.Server.Api/[API version]\" (required)
        :param str user_agent: The user agent of the calling client. (required)
        :param str ticket: The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the upload. (required)
        :param Object body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api', 'user_agent', 'ticket', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfer_controller_upload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api' is set
        if ('api' not in params or
                params['api'] is None):
            raise ValueError("Missing the required parameter `api` when calling `transfer_controller_upload`")  # noqa: E501
        # verify the required parameter 'user_agent' is set
        if ('user_agent' not in params or
                params['user_agent'] is None):
            raise ValueError("Missing the required parameter `user_agent` when calling `transfer_controller_upload`")  # noqa: E501
        # verify the required parameter 'ticket' is set
        if ('ticket' not in params or
                params['ticket'] is None):
            raise ValueError("Missing the required parameter `ticket` when calling `transfer_controller_upload`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ticket' in params:
            query_params.append(('ticket', params['ticket']))  # noqa: E501

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
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token_Authorization_Scheme']  # noqa: E501

        return self.api_client.call_api(
            '/Transfer', 'PUT',
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

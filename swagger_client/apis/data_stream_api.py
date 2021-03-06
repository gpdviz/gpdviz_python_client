# coding: utf-8

"""
    Gpdviz REST API

    The Gpdviz REST API deals with three main kinds of resources: sensor systems, data streams, and observations.

    OpenAPI spec version: 0.4.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DataStreamApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_stream(self, sysid, strid, **kwargs):
        """
        Delete a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_stream(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: DataStreamSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_stream_with_http_info(sysid, strid, **kwargs)
        else:
            (data) = self.delete_stream_with_http_info(sysid, strid, **kwargs)
            return data

    def delete_stream_with_http_info(self, sysid, strid, **kwargs):
        """
        Delete a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_stream_with_http_info(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: DataStreamSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sysid', 'strid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `delete_stream`")
        # verify the required parameter 'strid' is set
        if ('strid' not in params) or (params['strid'] is None):
            raise ValueError("Missing the required parameter `strid` when calling `delete_stream`")


        collection_formats = {}

        path_params = {}
        if 'sysid' in params:
            path_params['sysid'] = params['sysid']
        if 'strid' in params:
            path_params['strid'] = params['strid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ss/{sysid}/{strid}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataStreamSummary',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_stream(self, sysid, strid, **kwargs):
        """
        Get a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stream(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: DataStream
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_stream_with_http_info(sysid, strid, **kwargs)
        else:
            (data) = self.get_stream_with_http_info(sysid, strid, **kwargs)
            return data

    def get_stream_with_http_info(self, sysid, strid, **kwargs):
        """
        Get a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_stream_with_http_info(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: DataStream
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sysid', 'strid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `get_stream`")
        # verify the required parameter 'strid' is set
        if ('strid' not in params) or (params['strid'] is None):
            raise ValueError("Missing the required parameter `strid` when calling `get_stream`")


        collection_formats = {}

        path_params = {}
        if 'sysid' in params:
            path_params['sysid'] = params['sysid']
        if 'strid' in params:
            path_params['strid'] = params['strid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ss/{sysid}/{strid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataStream',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def register_stream(self, sysid, body, **kwargs):
        """
        Add a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.register_stream(sysid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param DataStreamAdd body: stream definition (required)
        :return: DataStreamSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.register_stream_with_http_info(sysid, body, **kwargs)
        else:
            (data) = self.register_stream_with_http_info(sysid, body, **kwargs)
            return data

    def register_stream_with_http_info(self, sysid, body, **kwargs):
        """
        Add a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.register_stream_with_http_info(sysid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param DataStreamAdd body: stream definition (required)
        :return: DataStreamSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sysid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method register_stream" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `register_stream`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `register_stream`")


        collection_formats = {}

        path_params = {}
        if 'sysid' in params:
            path_params['sysid'] = params['sysid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ss/{sysid}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DataStreamSummary',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

# coding: utf-8

"""
    

    gpdviz API

    OpenAPI spec version: 0.3.0
    
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

    def add_str(self, sysid, body, **kwargs):
        """
        Add a stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_str(sysid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param StreamRegister body: stream definition (required)
        :return: SensorSystem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_str_with_http_info(sysid, body, **kwargs)
        else:
            (data) = self.add_str_with_http_info(sysid, body, **kwargs)
            return data

    def add_str_with_http_info(self, sysid, body, **kwargs):
        """
        Add a stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_str_with_http_info(sysid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param StreamRegister body: stream definition (required)
        :return: SensorSystem
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
                    " to method add_str" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `add_str`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_str`")


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
                                        response_type='SensorSystem',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_str(self, sysid, strid, **kwargs):
        """
        Delete a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_str(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: SensorSystem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_str_with_http_info(sysid, strid, **kwargs)
        else:
            (data) = self.delete_str_with_http_info(sysid, strid, **kwargs)
            return data

    def delete_str_with_http_info(self, sysid, strid, **kwargs):
        """
        Delete a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_str_with_http_info(sysid, strid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :return: SensorSystem
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
                    " to method delete_str" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `delete_str`")
        # verify the required parameter 'strid' is set
        if ('strid' not in params) or (params['strid'] is None):
            raise ValueError("Missing the required parameter `strid` when calling `delete_str`")


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
                                        response_type='SensorSystem',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_str(self, sysid, strid, **kwargs):
        """
        Get a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_str(sysid, strid, callback=callback_function)

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
            return self.get_str_with_http_info(sysid, strid, **kwargs)
        else:
            (data) = self.get_str_with_http_info(sysid, strid, **kwargs)
            return data

    def get_str_with_http_info(self, sysid, strid, **kwargs):
        """
        Get a data stream
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_str_with_http_info(sysid, strid, callback=callback_function)

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
                    " to method get_str" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `get_str`")
        # verify the required parameter 'strid' is set
        if ('strid' not in params) or (params['strid'] is None):
            raise ValueError("Missing the required parameter `strid` when calling `get_str`")


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

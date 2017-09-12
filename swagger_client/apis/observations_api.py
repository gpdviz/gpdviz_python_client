# coding: utf-8

"""
    

     # Basic sequence  - Register a sensor system - `POST /ss` - Add one or more data streams to the sensor system - `POST /ss/{sysid}` - Add data stream observations - `POST /ss/{sysid}/{strid}/obs`        

    OpenAPI spec version: 0.3.1
    
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


class ObservationsApi(object):
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

    def add_observations(self, sysid, strid, body, **kwargs):
        """
        Add observations
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_observations(sysid, strid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :param ObservationsRegister body: The observations (required)
        :return: dict(str, float)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_observations_with_http_info(sysid, strid, body, **kwargs)
        else:
            (data) = self.add_observations_with_http_info(sysid, strid, body, **kwargs)
            return data

    def add_observations_with_http_info(self, sysid, strid, body, **kwargs):
        """
        Add observations
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_observations_with_http_info(sysid, strid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sysid: sensor system id (required)
        :param str strid: data stream id (required)
        :param ObservationsRegister body: The observations (required)
        :return: dict(str, float)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sysid', 'strid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_observations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sysid' is set
        if ('sysid' not in params) or (params['sysid'] is None):
            raise ValueError("Missing the required parameter `sysid` when calling `add_observations`")
        # verify the required parameter 'strid' is set
        if ('strid' not in params) or (params['strid'] is None):
            raise ValueError("Missing the required parameter `strid` when calling `add_observations`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_observations`")


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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/ss/{sysid}/{strid}/obs', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='dict(str, float)',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

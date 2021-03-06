# coding: utf-8

"""
    Gpdviz REST API

    The Gpdviz REST API deals with three main kinds of resources: sensor systems, data streams, and observations.

    OpenAPI spec version: 0.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.data_stream_api import DataStreamApi


class TestDataStreamApi(unittest.TestCase):
    """ DataStreamApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.data_stream_api.DataStreamApi()

    def tearDown(self):
        pass

    def test_delete_stream(self):
        """
        Test case for delete_stream

        Delete a data stream
        """
        pass

    def test_get_stream(self):
        """
        Test case for get_stream

        Get a data stream
        """
        pass

    def test_register_stream(self):
        """
        Test case for register_stream

        Add a data stream
        """
        pass


if __name__ == '__main__':
    unittest.main()

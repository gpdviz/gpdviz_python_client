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
from swagger_client.apis.sensor_system_api import SensorSystemApi


class TestSensorSystemApi(unittest.TestCase):
    """ SensorSystemApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.sensor_system_api.SensorSystemApi()

    def tearDown(self):
        pass

    def test_delete_system(self):
        """
        Test case for delete_system

        Unregister a sensor system
        """
        pass

    def test_get_system(self):
        """
        Test case for get_system

        Get a sensor system
        """
        pass

    def test_list_systems(self):
        """
        Test case for list_systems

        List all registered sensor systems
        """
        pass

    def test_register_stream(self):
        """
        Test case for register_stream

        Add a data stream
        """
        pass

    def test_register_system(self):
        """
        Test case for register_system

        Register sensor system
        """
        pass

    def test_update_system(self):
        """
        Test case for update_system

        Update a sensor system
        """
        pass


if __name__ == '__main__':
    unittest.main()

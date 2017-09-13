# coding: utf-8

"""
    

     # Basic sequence  - Register a sensor system - `POST /ss` - Add one or more data streams to the sensor system - `POST /ss/{sysid}` - Add data stream observations - `POST /ss/{sysid}/{strid}/obs`        

    OpenAPI spec version: 0.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.observations_api import ObservationsApi


class TestObservationsApi(unittest.TestCase):
    """ ObservationsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.observations_api.ObservationsApi()

    def tearDown(self):
        pass

    def test_add_observations(self):
        """
        Test case for add_observations

        Add observations
        """
        pass


if __name__ == '__main__':
    unittest.main()

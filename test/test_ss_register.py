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
from swagger_client.models.ss_register import SSRegister


class TestSSRegister(unittest.TestCase):
    """ SSRegister unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSSRegister(self):
        """
        Test SSRegister
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = swagger_client.models.ss_register.SSRegister()
        pass


if __name__ == '__main__':
    unittest.main()

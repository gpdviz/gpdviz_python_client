# coding: utf-8

"""
    

    gpdviz API

    OpenAPI spec version: 0.3.0
    
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

    def test_add_obs(self):
        """
        Test case for add_obs

        Add observations
        """
        pass


if __name__ == '__main__':
    unittest.main()
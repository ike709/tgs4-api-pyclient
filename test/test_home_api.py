# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 8.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.home_api import HomeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestHomeApi(unittest.TestCase):
    """HomeApi unit test stubs"""

    def setUp(self):
        self.api = HomeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_home_controller_create_token(self):
        """Test case for home_controller_create_token

        Attempt to authenticate a Tgstation.Server.Host.Models.User using Tgstation.Server.Host.Controllers.ApiController.ApiHeaders  # noqa: E501
        """
        pass

    def test_home_controller_home(self):
        """Test case for home_controller_home

        Main page of the Tgstation.Server.Host.Core.Application  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
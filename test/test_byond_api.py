# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 9.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.byond_api import ByondApi  # noqa: E501
from swagger_client.rest import ApiException


class TestByondApi(unittest.TestCase):
    """ByondApi unit test stubs"""

    def setUp(self):
        self.api = ByondApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_byond_controller_list(self):
        """Test case for byond_controller_list

        Lists installed Tgstation.Server.Api.Models.Response.ByondResponse.Versions.  # noqa: E501
        """
        pass

    def test_byond_controller_read(self):
        """Test case for byond_controller_read

        Gets the active Tgstation.Server.Api.Models.Response.ByondResponse.Version.  # noqa: E501
        """
        pass

    def test_byond_controller_update(self):
        """Test case for byond_controller_update

        Changes the active BYOND version to the one specified in a given model.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

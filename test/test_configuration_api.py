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
from swagger_client.api.configuration_api import ConfigurationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConfigurationApi(unittest.TestCase):
    """ConfigurationApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_configuration_controller_create_directory(self):
        """Test case for configuration_controller_create_directory

        Create a configuration directory.  # noqa: E501
        """
        pass

    def test_configuration_controller_delete_directory(self):
        """Test case for configuration_controller_delete_directory

        Deletes an empty directory  # noqa: E501
        """
        pass

    def test_configuration_controller_directory(self):
        """Test case for configuration_controller_directory

        Get the contents of a directory at a directoryPath  # noqa: E501
        """
        pass

    def test_configuration_controller_file(self):
        """Test case for configuration_controller_file

        Get the contents of a file at a filePath  # noqa: E501
        """
        pass

    def test_configuration_controller_list(self):
        """Test case for configuration_controller_list

        Get the contents of the root configuration directory.  # noqa: E501
        """
        pass

    def test_configuration_controller_update(self):
        """Test case for configuration_controller_update

        Write to a configuration file.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

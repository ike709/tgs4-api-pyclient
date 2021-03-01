# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 9.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdministrationResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tracked_repository_url': 'str',
        'latest_version': 'str'
    }

    attribute_map = {
        'tracked_repository_url': 'trackedRepositoryUrl',
        'latest_version': 'latestVersion'
    }

    def __init__(self, tracked_repository_url=None, latest_version=None):  # noqa: E501
        """AdministrationResponse - a model defined in Swagger"""  # noqa: E501
        self._tracked_repository_url = None
        self._latest_version = None
        self.discriminator = None
        if tracked_repository_url is not None:
            self.tracked_repository_url = tracked_repository_url
        if latest_version is not None:
            self.latest_version = latest_version

    @property
    def tracked_repository_url(self):
        """Gets the tracked_repository_url of this AdministrationResponse.  # noqa: E501

        The GitHub repository the server is built to recieve updates from  # noqa: E501

        :return: The tracked_repository_url of this AdministrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._tracked_repository_url

    @tracked_repository_url.setter
    def tracked_repository_url(self, tracked_repository_url):
        """Sets the tracked_repository_url of this AdministrationResponse.

        The GitHub repository the server is built to recieve updates from  # noqa: E501

        :param tracked_repository_url: The tracked_repository_url of this AdministrationResponse.  # noqa: E501
        :type: str
        """

        self._tracked_repository_url = tracked_repository_url

    @property
    def latest_version(self):
        """Gets the latest_version of this AdministrationResponse.  # noqa: E501

        The latest available version of the Tgstation.Server.Host assembly from the upstream repository. If System.Version.Major is not equal to 4 the update cannot be applied due to API changes  # noqa: E501

        :return: The latest_version of this AdministrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this AdministrationResponse.

        The latest available version of the Tgstation.Server.Host assembly from the upstream repository. If System.Version.Major is not equal to 4 the update cannot be applied due to API changes  # noqa: E501

        :param latest_version: The latest_version of this AdministrationResponse.  # noqa: E501
        :type: str
        """

        self._latest_version = latest_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdministrationResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdministrationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
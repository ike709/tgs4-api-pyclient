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

class ByondInstallResponse(object):
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
        'install_job': 'AllOfByondInstallResponseInstallJob',
        'file_ticket': 'str'
    }

    attribute_map = {
        'install_job': 'installJob',
        'file_ticket': 'fileTicket'
    }

    def __init__(self, install_job=None, file_ticket=None):  # noqa: E501
        """ByondInstallResponse - a model defined in Swagger"""  # noqa: E501
        self._install_job = None
        self._file_ticket = None
        self.discriminator = None
        if install_job is not None:
            self.install_job = install_job
        if file_ticket is not None:
            self.file_ticket = file_ticket

    @property
    def install_job(self):
        """Gets the install_job of this ByondInstallResponse.  # noqa: E501

        The Tgstation.Server.Api.Models.Response.JobResponse being used to install a new System.Version.  # noqa: E501

        :return: The install_job of this ByondInstallResponse.  # noqa: E501
        :rtype: AllOfByondInstallResponseInstallJob
        """
        return self._install_job

    @install_job.setter
    def install_job(self, install_job):
        """Sets the install_job of this ByondInstallResponse.

        The Tgstation.Server.Api.Models.Response.JobResponse being used to install a new System.Version.  # noqa: E501

        :param install_job: The install_job of this ByondInstallResponse.  # noqa: E501
        :type: AllOfByondInstallResponseInstallJob
        """

        self._install_job = install_job

    @property
    def file_ticket(self):
        """Gets the file_ticket of this ByondInstallResponse.  # noqa: E501


        :return: The file_ticket of this ByondInstallResponse.  # noqa: E501
        :rtype: str
        """
        return self._file_ticket

    @file_ticket.setter
    def file_ticket(self, file_ticket):
        """Sets the file_ticket of this ByondInstallResponse.


        :param file_ticket: The file_ticket of this ByondInstallResponse.  # noqa: E501
        :type: str
        """

        self._file_ticket = file_ticket

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
        if issubclass(ByondInstallResponse, dict):
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
        if not isinstance(other, ByondInstallResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

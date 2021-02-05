# coding: utf-8

"""
    TGS API

    A production scale tool for BYOND server management  # noqa: E501

    OpenAPI spec version: 8.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TestMergeParameters(object):
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
        'number': 'int',
        'target_commit_sha': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'number': 'number',
        'target_commit_sha': 'targetCommitSha',
        'comment': 'comment'
    }

    def __init__(self, number=None, target_commit_sha=None, comment=None):  # noqa: E501
        """TestMergeParameters - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._target_commit_sha = None
        self._comment = None
        self.discriminator = None
        if number is not None:
            self.number = number
        if target_commit_sha is not None:
            self.target_commit_sha = target_commit_sha
        if comment is not None:
            self.comment = comment

    @property
    def number(self):
        """Gets the number of this TestMergeParameters.  # noqa: E501

        The number of the test merge source.  # noqa: E501

        :return: The number of this TestMergeParameters.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TestMergeParameters.

        The number of the test merge source.  # noqa: E501

        :param number: The number of this TestMergeParameters.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def target_commit_sha(self):
        """Gets the target_commit_sha of this TestMergeParameters.  # noqa: E501

        The sha of the test merge revision to merge. If not specified, the latest commit shall be used (semi-unsafe)  # noqa: E501

        :return: The target_commit_sha of this TestMergeParameters.  # noqa: E501
        :rtype: str
        """
        return self._target_commit_sha

    @target_commit_sha.setter
    def target_commit_sha(self, target_commit_sha):
        """Sets the target_commit_sha of this TestMergeParameters.

        The sha of the test merge revision to merge. If not specified, the latest commit shall be used (semi-unsafe)  # noqa: E501

        :param target_commit_sha: The target_commit_sha of this TestMergeParameters.  # noqa: E501
        :type: str
        """

        self._target_commit_sha = target_commit_sha

    @property
    def comment(self):
        """Gets the comment of this TestMergeParameters.  # noqa: E501

        Optional comment about the test  # noqa: E501

        :return: The comment of this TestMergeParameters.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this TestMergeParameters.

        Optional comment about the test  # noqa: E501

        :param comment: The comment of this TestMergeParameters.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(TestMergeParameters, dict):
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
        if not isinstance(other, TestMergeParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

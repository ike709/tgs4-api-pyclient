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

class TestMerge(object):
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
        'merged_by': 'AllOfTestMergeMergedBy',
        'id': 'int',
        'merged_at': 'datetime',
        'title_at_merge': 'str',
        'body_at_merge': 'str',
        'url': 'str',
        'author': 'str',
        'number': 'int',
        'target_commit_sha': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'merged_by': 'mergedBy',
        'id': 'id',
        'merged_at': 'mergedAt',
        'title_at_merge': 'titleAtMerge',
        'body_at_merge': 'bodyAtMerge',
        'url': 'url',
        'author': 'author',
        'number': 'number',
        'target_commit_sha': 'targetCommitSha',
        'comment': 'comment'
    }

    def __init__(self, merged_by=None, id=None, merged_at=None, title_at_merge=None, body_at_merge=None, url=None, author=None, number=None, target_commit_sha=None, comment=None):  # noqa: E501
        """TestMerge - a model defined in Swagger"""  # noqa: E501
        self._merged_by = None
        self._id = None
        self._merged_at = None
        self._title_at_merge = None
        self._body_at_merge = None
        self._url = None
        self._author = None
        self._number = None
        self._target_commit_sha = None
        self._comment = None
        self.discriminator = None
        if merged_by is not None:
            self.merged_by = merged_by
        if id is not None:
            self.id = id
        if merged_at is not None:
            self.merged_at = merged_at
        if title_at_merge is not None:
            self.title_at_merge = title_at_merge
        if body_at_merge is not None:
            self.body_at_merge = body_at_merge
        if url is not None:
            self.url = url
        if author is not None:
            self.author = author
        if number is not None:
            self.number = number
        if target_commit_sha is not None:
            self.target_commit_sha = target_commit_sha
        if comment is not None:
            self.comment = comment

    @property
    def merged_by(self):
        """Gets the merged_by of this TestMerge.  # noqa: E501

        The Tgstation.Server.Api.Models.NamedEntity of the user who created the Tgstation.Server.Api.Models.TestMerge.  # noqa: E501

        :return: The merged_by of this TestMerge.  # noqa: E501
        :rtype: AllOfTestMergeMergedBy
        """
        return self._merged_by

    @merged_by.setter
    def merged_by(self, merged_by):
        """Sets the merged_by of this TestMerge.

        The Tgstation.Server.Api.Models.NamedEntity of the user who created the Tgstation.Server.Api.Models.TestMerge.  # noqa: E501

        :param merged_by: The merged_by of this TestMerge.  # noqa: E501
        :type: AllOfTestMergeMergedBy
        """

        self._merged_by = merged_by

    @property
    def id(self):
        """Gets the id of this TestMerge.  # noqa: E501

        The ID of the Tgstation.Server.Api.Models.Internal.TestMergeApiBase  # noqa: E501

        :return: The id of this TestMerge.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestMerge.

        The ID of the Tgstation.Server.Api.Models.Internal.TestMergeApiBase  # noqa: E501

        :param id: The id of this TestMerge.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def merged_at(self):
        """Gets the merged_at of this TestMerge.  # noqa: E501

        When the Tgstation.Server.Api.Models.Internal.TestMergeApiBase was created  # noqa: E501

        :return: The merged_at of this TestMerge.  # noqa: E501
        :rtype: datetime
        """
        return self._merged_at

    @merged_at.setter
    def merged_at(self, merged_at):
        """Sets the merged_at of this TestMerge.

        When the Tgstation.Server.Api.Models.Internal.TestMergeApiBase was created  # noqa: E501

        :param merged_at: The merged_at of this TestMerge.  # noqa: E501
        :type: datetime
        """

        self._merged_at = merged_at

    @property
    def title_at_merge(self):
        """Gets the title_at_merge of this TestMerge.  # noqa: E501

        The title of the test merge source.  # noqa: E501

        :return: The title_at_merge of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._title_at_merge

    @title_at_merge.setter
    def title_at_merge(self, title_at_merge):
        """Sets the title_at_merge of this TestMerge.

        The title of the test merge source.  # noqa: E501

        :param title_at_merge: The title_at_merge of this TestMerge.  # noqa: E501
        :type: str
        """

        self._title_at_merge = title_at_merge

    @property
    def body_at_merge(self):
        """Gets the body_at_merge of this TestMerge.  # noqa: E501

        The body of the test merge source.  # noqa: E501

        :return: The body_at_merge of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._body_at_merge

    @body_at_merge.setter
    def body_at_merge(self, body_at_merge):
        """Sets the body_at_merge of this TestMerge.

        The body of the test merge source.  # noqa: E501

        :param body_at_merge: The body_at_merge of this TestMerge.  # noqa: E501
        :type: str
        """

        self._body_at_merge = body_at_merge

    @property
    def url(self):
        """Gets the url of this TestMerge.  # noqa: E501

        The URL of the test merge source.  # noqa: E501

        :return: The url of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TestMerge.

        The URL of the test merge source.  # noqa: E501

        :param url: The url of this TestMerge.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def author(self):
        """Gets the author of this TestMerge.  # noqa: E501

        The author of the test merge source.  # noqa: E501

        :return: The author of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TestMerge.

        The author of the test merge source.  # noqa: E501

        :param author: The author of this TestMerge.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def number(self):
        """Gets the number of this TestMerge.  # noqa: E501

        The number of the test merge source.  # noqa: E501

        :return: The number of this TestMerge.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TestMerge.

        The number of the test merge source.  # noqa: E501

        :param number: The number of this TestMerge.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def target_commit_sha(self):
        """Gets the target_commit_sha of this TestMerge.  # noqa: E501

        The sha of the test merge revision to merge. If not specified, the latest commit shall be used (semi-unsafe)  # noqa: E501

        :return: The target_commit_sha of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._target_commit_sha

    @target_commit_sha.setter
    def target_commit_sha(self, target_commit_sha):
        """Sets the target_commit_sha of this TestMerge.

        The sha of the test merge revision to merge. If not specified, the latest commit shall be used (semi-unsafe)  # noqa: E501

        :param target_commit_sha: The target_commit_sha of this TestMerge.  # noqa: E501
        :type: str
        """

        self._target_commit_sha = target_commit_sha

    @property
    def comment(self):
        """Gets the comment of this TestMerge.  # noqa: E501

        Optional comment about the test  # noqa: E501

        :return: The comment of this TestMerge.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this TestMerge.

        Optional comment about the test  # noqa: E501

        :param comment: The comment of this TestMerge.  # noqa: E501
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
        if issubclass(TestMerge, dict):
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
        if not isinstance(other, TestMerge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class PaginatedLogFile(object):
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
        'content': 'list[LogFile]',
        'total_pages': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'content': 'content',
        'total_pages': 'totalPages',
        'page_size': 'pageSize'
    }

    def __init__(self, content=None, total_pages=None, page_size=None):  # noqa: E501
        """PaginatedLogFile - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._total_pages = None
        self._page_size = None
        self.discriminator = None
        if content is not None:
            self.content = content
        if total_pages is not None:
            self.total_pages = total_pages
        if page_size is not None:
            self.page_size = page_size

    @property
    def content(self):
        """Gets the content of this PaginatedLogFile.  # noqa: E501

        The System.Collections.Generic.ICollection`1 of the returned <typeparamref name=\"TModel\" />s.  # noqa: E501

        :return: The content of this PaginatedLogFile.  # noqa: E501
        :rtype: list[LogFile]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PaginatedLogFile.

        The System.Collections.Generic.ICollection`1 of the returned <typeparamref name=\"TModel\" />s.  # noqa: E501

        :param content: The content of this PaginatedLogFile.  # noqa: E501
        :type: list[LogFile]
        """

        self._content = content

    @property
    def total_pages(self):
        """Gets the total_pages of this PaginatedLogFile.  # noqa: E501

        The total number of pages in the query.  # noqa: E501

        :return: The total_pages of this PaginatedLogFile.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PaginatedLogFile.

        The total number of pages in the query.  # noqa: E501

        :param total_pages: The total_pages of this PaginatedLogFile.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def page_size(self):
        """Gets the page_size of this PaginatedLogFile.  # noqa: E501

        The current size of pages in the query.  # noqa: E501

        :return: The page_size of this PaginatedLogFile.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this PaginatedLogFile.

        The current size of pages in the query.  # noqa: E501

        :param page_size: The page_size of this PaginatedLogFile.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(PaginatedLogFile, dict):
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
        if not isinstance(other, PaginatedLogFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

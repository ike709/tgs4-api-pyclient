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

class InstanceResponse(object):
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
        'move_job': 'AllOfInstanceResponseMoveJob',
        'path': 'str',
        'online': 'bool',
        'configuration_type': 'AllOfInstanceResponseConfigurationType',
        'auto_update_interval': 'int',
        'chat_bot_limit': 'int',
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'move_job': 'moveJob',
        'path': 'path',
        'online': 'online',
        'configuration_type': 'configurationType',
        'auto_update_interval': 'autoUpdateInterval',
        'chat_bot_limit': 'chatBotLimit',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, move_job=None, path=None, online=None, configuration_type=None, auto_update_interval=None, chat_bot_limit=None, name=None, id=None):  # noqa: E501
        """InstanceResponse - a model defined in Swagger"""  # noqa: E501
        self._move_job = None
        self._path = None
        self._online = None
        self._configuration_type = None
        self._auto_update_interval = None
        self._chat_bot_limit = None
        self._name = None
        self._id = None
        self.discriminator = None
        if move_job is not None:
            self.move_job = move_job
        if path is not None:
            self.path = path
        if online is not None:
            self.online = online
        if configuration_type is not None:
            self.configuration_type = configuration_type
        if auto_update_interval is not None:
            self.auto_update_interval = auto_update_interval
        if chat_bot_limit is not None:
            self.chat_bot_limit = chat_bot_limit
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def move_job(self):
        """Gets the move_job of this InstanceResponse.  # noqa: E501

        The Tgstation.Server.Api.Models.Response.JobResponse representing a change of Tgstation.Server.Api.Models.Instance.Path.  # noqa: E501

        :return: The move_job of this InstanceResponse.  # noqa: E501
        :rtype: AllOfInstanceResponseMoveJob
        """
        return self._move_job

    @move_job.setter
    def move_job(self, move_job):
        """Sets the move_job of this InstanceResponse.

        The Tgstation.Server.Api.Models.Response.JobResponse representing a change of Tgstation.Server.Api.Models.Instance.Path.  # noqa: E501

        :param move_job: The move_job of this InstanceResponse.  # noqa: E501
        :type: AllOfInstanceResponseMoveJob
        """

        self._move_job = move_job

    @property
    def path(self):
        """Gets the path of this InstanceResponse.  # noqa: E501

        The path to where the Tgstation.Server.Api.Models.Instance is located. Can only be changed while the Tgstation.Server.Api.Models.Instance is offline. Must not exist when the instance is created  # noqa: E501

        :return: The path of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this InstanceResponse.

        The path to where the Tgstation.Server.Api.Models.Instance is located. Can only be changed while the Tgstation.Server.Api.Models.Instance is offline. Must not exist when the instance is created  # noqa: E501

        :param path: The path of this InstanceResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def online(self):
        """Gets the online of this InstanceResponse.  # noqa: E501

        If the Tgstation.Server.Api.Models.Instance is online  # noqa: E501

        :return: The online of this InstanceResponse.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this InstanceResponse.

        If the Tgstation.Server.Api.Models.Instance is online  # noqa: E501

        :param online: The online of this InstanceResponse.  # noqa: E501
        :type: bool
        """

        self._online = online

    @property
    def configuration_type(self):
        """Gets the configuration_type of this InstanceResponse.  # noqa: E501

        If Tgstation.Server.Api.Models.IConfigurationFiles can be used on the Tgstation.Server.Api.Models.Instance  # noqa: E501

        :return: The configuration_type of this InstanceResponse.  # noqa: E501
        :rtype: AllOfInstanceResponseConfigurationType
        """
        return self._configuration_type

    @configuration_type.setter
    def configuration_type(self, configuration_type):
        """Sets the configuration_type of this InstanceResponse.

        If Tgstation.Server.Api.Models.IConfigurationFiles can be used on the Tgstation.Server.Api.Models.Instance  # noqa: E501

        :param configuration_type: The configuration_type of this InstanceResponse.  # noqa: E501
        :type: AllOfInstanceResponseConfigurationType
        """

        self._configuration_type = configuration_type

    @property
    def auto_update_interval(self):
        """Gets the auto_update_interval of this InstanceResponse.  # noqa: E501

        The time interval in minutes the repository is automatically pulled and compiles. 0 disables  # noqa: E501

        :return: The auto_update_interval of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._auto_update_interval

    @auto_update_interval.setter
    def auto_update_interval(self, auto_update_interval):
        """Sets the auto_update_interval of this InstanceResponse.

        The time interval in minutes the repository is automatically pulled and compiles. 0 disables  # noqa: E501

        :param auto_update_interval: The auto_update_interval of this InstanceResponse.  # noqa: E501
        :type: int
        """

        self._auto_update_interval = auto_update_interval

    @property
    def chat_bot_limit(self):
        """Gets the chat_bot_limit of this InstanceResponse.  # noqa: E501

        The maximum number of chat bots the Tgstation.Server.Api.Models.Instance may contain.  # noqa: E501

        :return: The chat_bot_limit of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._chat_bot_limit

    @chat_bot_limit.setter
    def chat_bot_limit(self, chat_bot_limit):
        """Sets the chat_bot_limit of this InstanceResponse.

        The maximum number of chat bots the Tgstation.Server.Api.Models.Instance may contain.  # noqa: E501

        :param chat_bot_limit: The chat_bot_limit of this InstanceResponse.  # noqa: E501
        :type: int
        """

        self._chat_bot_limit = chat_bot_limit

    @property
    def name(self):
        """Gets the name of this InstanceResponse.  # noqa: E501

        The name of the entity represented by the Tgstation.Server.Api.Models.NamedEntity.  # noqa: E501

        :return: The name of this InstanceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceResponse.

        The name of the entity represented by the Tgstation.Server.Api.Models.NamedEntity.  # noqa: E501

        :param name: The name of this InstanceResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this InstanceResponse.  # noqa: E501

        The ID of the entity.  # noqa: E501

        :return: The id of this InstanceResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceResponse.

        The ID of the entity.  # noqa: E501

        :param id: The id of this InstanceResponse.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(InstanceResponse, dict):
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
        if not isinstance(other, InstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

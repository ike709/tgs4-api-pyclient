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

class UserUpdateRequest(object):
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
        'password': 'str',
        'o_auth_connections': 'list[OAuthConnection]',
        'permission_set': 'AllOfUserUpdateRequestPermissionSet',
        'group': 'AllOfUserUpdateRequestGroup',
        'enabled': 'bool',
        'system_identifier': 'str',
        'name': 'str',
        'id': 'int'
    }

    attribute_map = {
        'password': 'password',
        'o_auth_connections': 'oAuthConnections',
        'permission_set': 'permissionSet',
        'group': 'group',
        'enabled': 'enabled',
        'system_identifier': 'systemIdentifier',
        'name': 'name',
        'id': 'id'
    }

    def __init__(self, password=None, o_auth_connections=None, permission_set=None, group=None, enabled=None, system_identifier=None, name=None, id=None):  # noqa: E501
        """UserUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._o_auth_connections = None
        self._permission_set = None
        self._group = None
        self._enabled = None
        self._system_identifier = None
        self._name = None
        self._id = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if o_auth_connections is not None:
            self.o_auth_connections = o_auth_connections
        if permission_set is not None:
            self.permission_set = permission_set
        if group is not None:
            self.group = group
        if enabled is not None:
            self.enabled = enabled
        if system_identifier is not None:
            self.system_identifier = system_identifier
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id

    @property
    def password(self):
        """Gets the password of this UserUpdateRequest.  # noqa: E501

        Cleartext password of the user.  # noqa: E501

        :return: The password of this UserUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserUpdateRequest.

        Cleartext password of the user.  # noqa: E501

        :param password: The password of this UserUpdateRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def o_auth_connections(self):
        """Gets the o_auth_connections of this UserUpdateRequest.  # noqa: E501

        List of Tgstation.Server.Api.Models.OAuthConnections associated with the user.  # noqa: E501

        :return: The o_auth_connections of this UserUpdateRequest.  # noqa: E501
        :rtype: list[OAuthConnection]
        """
        return self._o_auth_connections

    @o_auth_connections.setter
    def o_auth_connections(self, o_auth_connections):
        """Sets the o_auth_connections of this UserUpdateRequest.

        List of Tgstation.Server.Api.Models.OAuthConnections associated with the user.  # noqa: E501

        :param o_auth_connections: The o_auth_connections of this UserUpdateRequest.  # noqa: E501
        :type: list[OAuthConnection]
        """

        self._o_auth_connections = o_auth_connections

    @property
    def permission_set(self):
        """Gets the permission_set of this UserUpdateRequest.  # noqa: E501

        The Tgstation.Server.Api.Models.PermissionSet directly associated with the user.  # noqa: E501

        :return: The permission_set of this UserUpdateRequest.  # noqa: E501
        :rtype: AllOfUserUpdateRequestPermissionSet
        """
        return self._permission_set

    @permission_set.setter
    def permission_set(self, permission_set):
        """Sets the permission_set of this UserUpdateRequest.

        The Tgstation.Server.Api.Models.PermissionSet directly associated with the user.  # noqa: E501

        :param permission_set: The permission_set of this UserUpdateRequest.  # noqa: E501
        :type: AllOfUserUpdateRequestPermissionSet
        """

        self._permission_set = permission_set

    @property
    def group(self):
        """Gets the group of this UserUpdateRequest.  # noqa: E501

        The Tgstation.Server.Api.Models.Internal.UserGroup asociated with the user, if any.  # noqa: E501

        :return: The group of this UserUpdateRequest.  # noqa: E501
        :rtype: AllOfUserUpdateRequestGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UserUpdateRequest.

        The Tgstation.Server.Api.Models.Internal.UserGroup asociated with the user, if any.  # noqa: E501

        :param group: The group of this UserUpdateRequest.  # noqa: E501
        :type: AllOfUserUpdateRequestGroup
        """

        self._group = group

    @property
    def enabled(self):
        """Gets the enabled of this UserUpdateRequest.  # noqa: E501

        If the Tgstation.Server.Api.Models.Internal.UserModelBase is enabled since users cannot be deleted. System users cannot be disabled  # noqa: E501

        :return: The enabled of this UserUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserUpdateRequest.

        If the Tgstation.Server.Api.Models.Internal.UserModelBase is enabled since users cannot be deleted. System users cannot be disabled  # noqa: E501

        :param enabled: The enabled of this UserUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def system_identifier(self):
        """Gets the system_identifier of this UserUpdateRequest.  # noqa: E501

        The SID/UID of the Tgstation.Server.Api.Models.Internal.UserModelBase on Windows/POSIX respectively  # noqa: E501

        :return: The system_identifier of this UserUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._system_identifier

    @system_identifier.setter
    def system_identifier(self, system_identifier):
        """Sets the system_identifier of this UserUpdateRequest.

        The SID/UID of the Tgstation.Server.Api.Models.Internal.UserModelBase on Windows/POSIX respectively  # noqa: E501

        :param system_identifier: The system_identifier of this UserUpdateRequest.  # noqa: E501
        :type: str
        """

        self._system_identifier = system_identifier

    @property
    def name(self):
        """Gets the name of this UserUpdateRequest.  # noqa: E501


        :return: The name of this UserUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserUpdateRequest.


        :param name: The name of this UserUpdateRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this UserUpdateRequest.  # noqa: E501

        The ID of the entity.  # noqa: E501

        :return: The id of this UserUpdateRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserUpdateRequest.

        The ID of the entity.  # noqa: E501

        :param id: The id of this UserUpdateRequest.  # noqa: E501
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
        if issubclass(UserUpdateRequest, dict):
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
        if not isinstance(other, UserUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

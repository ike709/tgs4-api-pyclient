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

class InstancePermissionSetResponse(object):
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
        'permission_set_id': 'int',
        'instance_permission_set_rights': 'AllOfInstancePermissionSetResponseInstancePermissionSetRights',
        'byond_rights': 'AllOfInstancePermissionSetResponseByondRights',
        'dream_daemon_rights': 'AllOfInstancePermissionSetResponseDreamDaemonRights',
        'dream_maker_rights': 'AllOfInstancePermissionSetResponseDreamMakerRights',
        'repository_rights': 'AllOfInstancePermissionSetResponseRepositoryRights',
        'chat_bot_rights': 'AllOfInstancePermissionSetResponseChatBotRights',
        'configuration_rights': 'AllOfInstancePermissionSetResponseConfigurationRights'
    }

    attribute_map = {
        'permission_set_id': 'permissionSetId',
        'instance_permission_set_rights': 'instancePermissionSetRights',
        'byond_rights': 'byondRights',
        'dream_daemon_rights': 'dreamDaemonRights',
        'dream_maker_rights': 'dreamMakerRights',
        'repository_rights': 'repositoryRights',
        'chat_bot_rights': 'chatBotRights',
        'configuration_rights': 'configurationRights'
    }

    def __init__(self, permission_set_id=None, instance_permission_set_rights=None, byond_rights=None, dream_daemon_rights=None, dream_maker_rights=None, repository_rights=None, chat_bot_rights=None, configuration_rights=None):  # noqa: E501
        """InstancePermissionSetResponse - a model defined in Swagger"""  # noqa: E501
        self._permission_set_id = None
        self._instance_permission_set_rights = None
        self._byond_rights = None
        self._dream_daemon_rights = None
        self._dream_maker_rights = None
        self._repository_rights = None
        self._chat_bot_rights = None
        self._configuration_rights = None
        self.discriminator = None
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if instance_permission_set_rights is not None:
            self.instance_permission_set_rights = instance_permission_set_rights
        if byond_rights is not None:
            self.byond_rights = byond_rights
        if dream_daemon_rights is not None:
            self.dream_daemon_rights = dream_daemon_rights
        if dream_maker_rights is not None:
            self.dream_maker_rights = dream_maker_rights
        if repository_rights is not None:
            self.repository_rights = repository_rights
        if chat_bot_rights is not None:
            self.chat_bot_rights = chat_bot_rights
        if configuration_rights is not None:
            self.configuration_rights = configuration_rights

    @property
    def permission_set_id(self):
        """Gets the permission_set_id of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.PermissionSet the Tgstation.Server.Api.Models.Internal.InstancePermissionSet belongs to  # noqa: E501

        :return: The permission_set_id of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: int
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        """Sets the permission_set_id of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.PermissionSet the Tgstation.Server.Api.Models.Internal.InstancePermissionSet belongs to  # noqa: E501

        :param permission_set_id: The permission_set_id of this InstancePermissionSetResponse.  # noqa: E501
        :type: int
        """

        self._permission_set_id = permission_set_id

    @property
    def instance_permission_set_rights(self):
        """Gets the instance_permission_set_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.InstancePermissionSetRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The instance_permission_set_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseInstancePermissionSetRights
        """
        return self._instance_permission_set_rights

    @instance_permission_set_rights.setter
    def instance_permission_set_rights(self, instance_permission_set_rights):
        """Sets the instance_permission_set_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.InstancePermissionSetRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param instance_permission_set_rights: The instance_permission_set_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseInstancePermissionSetRights
        """

        self._instance_permission_set_rights = instance_permission_set_rights

    @property
    def byond_rights(self):
        """Gets the byond_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.ByondRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The byond_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseByondRights
        """
        return self._byond_rights

    @byond_rights.setter
    def byond_rights(self, byond_rights):
        """Sets the byond_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.ByondRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param byond_rights: The byond_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseByondRights
        """

        self._byond_rights = byond_rights

    @property
    def dream_daemon_rights(self):
        """Gets the dream_daemon_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.DreamDaemonRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The dream_daemon_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseDreamDaemonRights
        """
        return self._dream_daemon_rights

    @dream_daemon_rights.setter
    def dream_daemon_rights(self, dream_daemon_rights):
        """Sets the dream_daemon_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.DreamDaemonRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param dream_daemon_rights: The dream_daemon_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseDreamDaemonRights
        """

        self._dream_daemon_rights = dream_daemon_rights

    @property
    def dream_maker_rights(self):
        """Gets the dream_maker_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.DreamMakerRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The dream_maker_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseDreamMakerRights
        """
        return self._dream_maker_rights

    @dream_maker_rights.setter
    def dream_maker_rights(self, dream_maker_rights):
        """Sets the dream_maker_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.DreamMakerRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param dream_maker_rights: The dream_maker_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseDreamMakerRights
        """

        self._dream_maker_rights = dream_maker_rights

    @property
    def repository_rights(self):
        """Gets the repository_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.RepositoryRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The repository_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseRepositoryRights
        """
        return self._repository_rights

    @repository_rights.setter
    def repository_rights(self, repository_rights):
        """Sets the repository_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.RepositoryRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param repository_rights: The repository_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseRepositoryRights
        """

        self._repository_rights = repository_rights

    @property
    def chat_bot_rights(self):
        """Gets the chat_bot_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.ChatBotRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The chat_bot_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseChatBotRights
        """
        return self._chat_bot_rights

    @chat_bot_rights.setter
    def chat_bot_rights(self, chat_bot_rights):
        """Sets the chat_bot_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.ChatBotRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param chat_bot_rights: The chat_bot_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseChatBotRights
        """

        self._chat_bot_rights = chat_bot_rights

    @property
    def configuration_rights(self):
        """Gets the configuration_rights of this InstancePermissionSetResponse.  # noqa: E501

        The Tgstation.Server.Api.Rights.ConfigurationRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :return: The configuration_rights of this InstancePermissionSetResponse.  # noqa: E501
        :rtype: AllOfInstancePermissionSetResponseConfigurationRights
        """
        return self._configuration_rights

    @configuration_rights.setter
    def configuration_rights(self, configuration_rights):
        """Sets the configuration_rights of this InstancePermissionSetResponse.

        The Tgstation.Server.Api.Rights.ConfigurationRights of the Tgstation.Server.Api.Models.Internal.InstancePermissionSet  # noqa: E501

        :param configuration_rights: The configuration_rights of this InstancePermissionSetResponse.  # noqa: E501
        :type: AllOfInstancePermissionSetResponseConfigurationRights
        """

        self._configuration_rights = configuration_rights

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
        if issubclass(InstancePermissionSetResponse, dict):
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
        if not isinstance(other, InstancePermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

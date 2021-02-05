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

class ServerInformation(object):
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
        'version': 'str',
        'api_version': 'str',
        'dm_api_version': 'str',
        'windows_host': 'bool',
        'update_in_progress': 'bool',
        'swarm_servers': 'list[SwarmServer]',
        'o_auth_provider_infos': 'ServerInformationOAuthProviderInfos',
        'minimum_password_length': 'int',
        'instance_limit': 'int',
        'user_limit': 'int',
        'user_group_limit': 'int',
        'valid_instance_paths': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'api_version': 'apiVersion',
        'dm_api_version': 'dmApiVersion',
        'windows_host': 'windowsHost',
        'update_in_progress': 'updateInProgress',
        'swarm_servers': 'swarmServers',
        'o_auth_provider_infos': 'oAuthProviderInfos',
        'minimum_password_length': 'minimumPasswordLength',
        'instance_limit': 'instanceLimit',
        'user_limit': 'userLimit',
        'user_group_limit': 'userGroupLimit',
        'valid_instance_paths': 'validInstancePaths'
    }

    def __init__(self, version=None, api_version=None, dm_api_version=None, windows_host=None, update_in_progress=None, swarm_servers=None, o_auth_provider_infos=None, minimum_password_length=None, instance_limit=None, user_limit=None, user_group_limit=None, valid_instance_paths=None):  # noqa: E501
        """ServerInformation - a model defined in Swagger"""  # noqa: E501
        self._version = None
        self._api_version = None
        self._dm_api_version = None
        self._windows_host = None
        self._update_in_progress = None
        self._swarm_servers = None
        self._o_auth_provider_infos = None
        self._minimum_password_length = None
        self._instance_limit = None
        self._user_limit = None
        self._user_group_limit = None
        self._valid_instance_paths = None
        self.discriminator = None
        if version is not None:
            self.version = version
        if api_version is not None:
            self.api_version = api_version
        if dm_api_version is not None:
            self.dm_api_version = dm_api_version
        if windows_host is not None:
            self.windows_host = windows_host
        if update_in_progress is not None:
            self.update_in_progress = update_in_progress
        if swarm_servers is not None:
            self.swarm_servers = swarm_servers
        if o_auth_provider_infos is not None:
            self.o_auth_provider_infos = o_auth_provider_infos
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if instance_limit is not None:
            self.instance_limit = instance_limit
        if user_limit is not None:
            self.user_limit = user_limit
        if user_group_limit is not None:
            self.user_group_limit = user_group_limit
        if valid_instance_paths is not None:
            self.valid_instance_paths = valid_instance_paths

    @property
    def version(self):
        """Gets the version of this ServerInformation.  # noqa: E501

        The version of the host  # noqa: E501

        :return: The version of this ServerInformation.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServerInformation.

        The version of the host  # noqa: E501

        :param version: The version of this ServerInformation.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def api_version(self):
        """Gets the api_version of this ServerInformation.  # noqa: E501

        The N:Tgstation.Server.Api version of the host  # noqa: E501

        :return: The api_version of this ServerInformation.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ServerInformation.

        The N:Tgstation.Server.Api version of the host  # noqa: E501

        :param api_version: The api_version of this ServerInformation.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def dm_api_version(self):
        """Gets the dm_api_version of this ServerInformation.  # noqa: E501

        The DMAPI interop version the server uses.  # noqa: E501

        :return: The dm_api_version of this ServerInformation.  # noqa: E501
        :rtype: str
        """
        return self._dm_api_version

    @dm_api_version.setter
    def dm_api_version(self, dm_api_version):
        """Sets the dm_api_version of this ServerInformation.

        The DMAPI interop version the server uses.  # noqa: E501

        :param dm_api_version: The dm_api_version of this ServerInformation.  # noqa: E501
        :type: str
        """

        self._dm_api_version = dm_api_version

    @property
    def windows_host(self):
        """Gets the windows_host of this ServerInformation.  # noqa: E501

        If the server is running on a windows operating system.  # noqa: E501

        :return: The windows_host of this ServerInformation.  # noqa: E501
        :rtype: bool
        """
        return self._windows_host

    @windows_host.setter
    def windows_host(self, windows_host):
        """Sets the windows_host of this ServerInformation.

        If the server is running on a windows operating system.  # noqa: E501

        :param windows_host: The windows_host of this ServerInformation.  # noqa: E501
        :type: bool
        """

        self._windows_host = windows_host

    @property
    def update_in_progress(self):
        """Gets the update_in_progress of this ServerInformation.  # noqa: E501

        If there is a server update in progress.  # noqa: E501

        :return: The update_in_progress of this ServerInformation.  # noqa: E501
        :rtype: bool
        """
        return self._update_in_progress

    @update_in_progress.setter
    def update_in_progress(self, update_in_progress):
        """Sets the update_in_progress of this ServerInformation.

        If there is a server update in progress.  # noqa: E501

        :param update_in_progress: The update_in_progress of this ServerInformation.  # noqa: E501
        :type: bool
        """

        self._update_in_progress = update_in_progress

    @property
    def swarm_servers(self):
        """Gets the swarm_servers of this ServerInformation.  # noqa: E501

        A System.Collections.Generic.ICollection`1 of connected Tgstation.Server.Api.Models.SwarmServers.  # noqa: E501

        :return: The swarm_servers of this ServerInformation.  # noqa: E501
        :rtype: list[SwarmServer]
        """
        return self._swarm_servers

    @swarm_servers.setter
    def swarm_servers(self, swarm_servers):
        """Sets the swarm_servers of this ServerInformation.

        A System.Collections.Generic.ICollection`1 of connected Tgstation.Server.Api.Models.SwarmServers.  # noqa: E501

        :param swarm_servers: The swarm_servers of this ServerInformation.  # noqa: E501
        :type: list[SwarmServer]
        """

        self._swarm_servers = swarm_servers

    @property
    def o_auth_provider_infos(self):
        """Gets the o_auth_provider_infos of this ServerInformation.  # noqa: E501


        :return: The o_auth_provider_infos of this ServerInformation.  # noqa: E501
        :rtype: ServerInformationOAuthProviderInfos
        """
        return self._o_auth_provider_infos

    @o_auth_provider_infos.setter
    def o_auth_provider_infos(self, o_auth_provider_infos):
        """Sets the o_auth_provider_infos of this ServerInformation.


        :param o_auth_provider_infos: The o_auth_provider_infos of this ServerInformation.  # noqa: E501
        :type: ServerInformationOAuthProviderInfos
        """

        self._o_auth_provider_infos = o_auth_provider_infos

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this ServerInformation.  # noqa: E501

        Minimum length of database user passwords.  # noqa: E501

        :return: The minimum_password_length of this ServerInformation.  # noqa: E501
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this ServerInformation.

        Minimum length of database user passwords.  # noqa: E501

        :param minimum_password_length: The minimum_password_length of this ServerInformation.  # noqa: E501
        :type: int
        """

        self._minimum_password_length = minimum_password_length

    @property
    def instance_limit(self):
        """Gets the instance_limit of this ServerInformation.  # noqa: E501

        The maximum number of Tgstation.Server.Api.Models.Instances allowed.  # noqa: E501

        :return: The instance_limit of this ServerInformation.  # noqa: E501
        :rtype: int
        """
        return self._instance_limit

    @instance_limit.setter
    def instance_limit(self, instance_limit):
        """Sets the instance_limit of this ServerInformation.

        The maximum number of Tgstation.Server.Api.Models.Instances allowed.  # noqa: E501

        :param instance_limit: The instance_limit of this ServerInformation.  # noqa: E501
        :type: int
        """

        self._instance_limit = instance_limit

    @property
    def user_limit(self):
        """Gets the user_limit of this ServerInformation.  # noqa: E501

        The maximum number of Tgstation.Server.Api.Models.Users allowed.  # noqa: E501

        :return: The user_limit of this ServerInformation.  # noqa: E501
        :rtype: int
        """
        return self._user_limit

    @user_limit.setter
    def user_limit(self, user_limit):
        """Sets the user_limit of this ServerInformation.

        The maximum number of Tgstation.Server.Api.Models.Users allowed.  # noqa: E501

        :param user_limit: The user_limit of this ServerInformation.  # noqa: E501
        :type: int
        """

        self._user_limit = user_limit

    @property
    def user_group_limit(self):
        """Gets the user_group_limit of this ServerInformation.  # noqa: E501

        The maximum number of Tgstation.Server.Api.Models.UserGroups allowed.  # noqa: E501

        :return: The user_group_limit of this ServerInformation.  # noqa: E501
        :rtype: int
        """
        return self._user_group_limit

    @user_group_limit.setter
    def user_group_limit(self, user_group_limit):
        """Sets the user_group_limit of this ServerInformation.

        The maximum number of Tgstation.Server.Api.Models.UserGroups allowed.  # noqa: E501

        :param user_group_limit: The user_group_limit of this ServerInformation.  # noqa: E501
        :type: int
        """

        self._user_group_limit = user_group_limit

    @property
    def valid_instance_paths(self):
        """Gets the valid_instance_paths of this ServerInformation.  # noqa: E501

        Limits the locations instances may be created or attached from.  # noqa: E501

        :return: The valid_instance_paths of this ServerInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_instance_paths

    @valid_instance_paths.setter
    def valid_instance_paths(self, valid_instance_paths):
        """Sets the valid_instance_paths of this ServerInformation.

        Limits the locations instances may be created or attached from.  # noqa: E501

        :param valid_instance_paths: The valid_instance_paths of this ServerInformation.  # noqa: E501
        :type: list[str]
        """

        self._valid_instance_paths = valid_instance_paths

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
        if issubclass(ServerInformation, dict):
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
        if not isinstance(other, ServerInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
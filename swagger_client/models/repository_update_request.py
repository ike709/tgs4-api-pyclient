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

class RepositoryUpdateRequest(object):
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
        'checkout_sha': 'str',
        'update_from_origin': 'bool',
        'new_test_merges': 'list[TestMergeParameters]',
        'reference': 'str',
        'committer_name': 'str',
        'committer_email': 'str',
        'access_user': 'str',
        'access_token': 'str',
        'push_test_merge_commits': 'bool',
        'create_git_hub_deployments': 'bool',
        'show_test_merge_committers': 'bool',
        'auto_updates_keep_test_merges': 'bool',
        'auto_updates_synchronize': 'bool',
        'post_test_merge_comment': 'bool'
    }

    attribute_map = {
        'checkout_sha': 'checkoutSha',
        'update_from_origin': 'updateFromOrigin',
        'new_test_merges': 'newTestMerges',
        'reference': 'reference',
        'committer_name': 'committerName',
        'committer_email': 'committerEmail',
        'access_user': 'accessUser',
        'access_token': 'accessToken',
        'push_test_merge_commits': 'pushTestMergeCommits',
        'create_git_hub_deployments': 'createGitHubDeployments',
        'show_test_merge_committers': 'showTestMergeCommitters',
        'auto_updates_keep_test_merges': 'autoUpdatesKeepTestMerges',
        'auto_updates_synchronize': 'autoUpdatesSynchronize',
        'post_test_merge_comment': 'postTestMergeComment'
    }

    def __init__(self, checkout_sha=None, update_from_origin=None, new_test_merges=None, reference=None, committer_name=None, committer_email=None, access_user=None, access_token=None, push_test_merge_commits=None, create_git_hub_deployments=None, show_test_merge_committers=None, auto_updates_keep_test_merges=None, auto_updates_synchronize=None, post_test_merge_comment=None):  # noqa: E501
        """RepositoryUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._checkout_sha = None
        self._update_from_origin = None
        self._new_test_merges = None
        self._reference = None
        self._committer_name = None
        self._committer_email = None
        self._access_user = None
        self._access_token = None
        self._push_test_merge_commits = None
        self._create_git_hub_deployments = None
        self._show_test_merge_committers = None
        self._auto_updates_keep_test_merges = None
        self._auto_updates_synchronize = None
        self._post_test_merge_comment = None
        self.discriminator = None
        if checkout_sha is not None:
            self.checkout_sha = checkout_sha
        if update_from_origin is not None:
            self.update_from_origin = update_from_origin
        if new_test_merges is not None:
            self.new_test_merges = new_test_merges
        if reference is not None:
            self.reference = reference
        if committer_name is not None:
            self.committer_name = committer_name
        if committer_email is not None:
            self.committer_email = committer_email
        if access_user is not None:
            self.access_user = access_user
        if access_token is not None:
            self.access_token = access_token
        if push_test_merge_commits is not None:
            self.push_test_merge_commits = push_test_merge_commits
        if create_git_hub_deployments is not None:
            self.create_git_hub_deployments = create_git_hub_deployments
        if show_test_merge_committers is not None:
            self.show_test_merge_committers = show_test_merge_committers
        if auto_updates_keep_test_merges is not None:
            self.auto_updates_keep_test_merges = auto_updates_keep_test_merges
        if auto_updates_synchronize is not None:
            self.auto_updates_synchronize = auto_updates_synchronize
        if post_test_merge_comment is not None:
            self.post_test_merge_comment = post_test_merge_comment

    @property
    def checkout_sha(self):
        """Gets the checkout_sha of this RepositoryUpdateRequest.  # noqa: E501

        The commit HEAD should point to.  # noqa: E501

        :return: The checkout_sha of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._checkout_sha

    @checkout_sha.setter
    def checkout_sha(self, checkout_sha):
        """Sets the checkout_sha of this RepositoryUpdateRequest.

        The commit HEAD should point to.  # noqa: E501

        :param checkout_sha: The checkout_sha of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._checkout_sha = checkout_sha

    @property
    def update_from_origin(self):
        """Gets the update_from_origin of this RepositoryUpdateRequest.  # noqa: E501

        Do the equivalent of a git pull. Will attempt to merge unless Tgstation.Server.Api.Models.Internal.RepositoryApiBase.Reference is also specified in which case a hard reset will be performed after checking out  # noqa: E501

        :return: The update_from_origin of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._update_from_origin

    @update_from_origin.setter
    def update_from_origin(self, update_from_origin):
        """Sets the update_from_origin of this RepositoryUpdateRequest.

        Do the equivalent of a git pull. Will attempt to merge unless Tgstation.Server.Api.Models.Internal.RepositoryApiBase.Reference is also specified in which case a hard reset will be performed after checking out  # noqa: E501

        :param update_from_origin: The update_from_origin of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._update_from_origin = update_from_origin

    @property
    def new_test_merges(self):
        """Gets the new_test_merges of this RepositoryUpdateRequest.  # noqa: E501

        Tgstation.Server.Api.Models.TestMergeParameters for new Tgstation.Server.Api.Models.TestMerges. Note that merges that conflict will not be performed  # noqa: E501

        :return: The new_test_merges of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: list[TestMergeParameters]
        """
        return self._new_test_merges

    @new_test_merges.setter
    def new_test_merges(self, new_test_merges):
        """Sets the new_test_merges of this RepositoryUpdateRequest.

        Tgstation.Server.Api.Models.TestMergeParameters for new Tgstation.Server.Api.Models.TestMerges. Note that merges that conflict will not be performed  # noqa: E501

        :param new_test_merges: The new_test_merges of this RepositoryUpdateRequest.  # noqa: E501
        :type: list[TestMergeParameters]
        """

        self._new_test_merges = new_test_merges

    @property
    def reference(self):
        """Gets the reference of this RepositoryUpdateRequest.  # noqa: E501

        The branch or tag HEAD points to.  # noqa: E501

        :return: The reference of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this RepositoryUpdateRequest.

        The branch or tag HEAD points to.  # noqa: E501

        :param reference: The reference of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def committer_name(self):
        """Gets the committer_name of this RepositoryUpdateRequest.  # noqa: E501

        The name of the committer  # noqa: E501

        :return: The committer_name of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """Sets the committer_name of this RepositoryUpdateRequest.

        The name of the committer  # noqa: E501

        :param committer_name: The committer_name of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._committer_name = committer_name

    @property
    def committer_email(self):
        """Gets the committer_email of this RepositoryUpdateRequest.  # noqa: E501

        The e-mail of the committer  # noqa: E501

        :return: The committer_email of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """Sets the committer_email of this RepositoryUpdateRequest.

        The e-mail of the committer  # noqa: E501

        :param committer_email: The committer_email of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._committer_email = committer_email

    @property
    def access_user(self):
        """Gets the access_user of this RepositoryUpdateRequest.  # noqa: E501

        The username to access the git repository with  # noqa: E501

        :return: The access_user of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this RepositoryUpdateRequest.

        The username to access the git repository with  # noqa: E501

        :param access_user: The access_user of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._access_user = access_user

    @property
    def access_token(self):
        """Gets the access_token of this RepositoryUpdateRequest.  # noqa: E501

        The token/password to access the git repository with  # noqa: E501

        :return: The access_token of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this RepositoryUpdateRequest.

        The token/password to access the git repository with  # noqa: E501

        :param access_token: The access_token of this RepositoryUpdateRequest.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def push_test_merge_commits(self):
        """Gets the push_test_merge_commits of this RepositoryUpdateRequest.  # noqa: E501

        If commits created from testmerges are pushed to the remote. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The push_test_merge_commits of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._push_test_merge_commits

    @push_test_merge_commits.setter
    def push_test_merge_commits(self, push_test_merge_commits):
        """Sets the push_test_merge_commits of this RepositoryUpdateRequest.

        If commits created from testmerges are pushed to the remote. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param push_test_merge_commits: The push_test_merge_commits of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._push_test_merge_commits = push_test_merge_commits

    @property
    def create_git_hub_deployments(self):
        """Gets the create_git_hub_deployments of this RepositoryUpdateRequest.  # noqa: E501

        If GitHub deployments should be created. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser, Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken, and Tgstation.Server.Api.Models.Internal.RepositorySettings.PushTestMergeCommits to be set to function.  # noqa: E501

        :return: The create_git_hub_deployments of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._create_git_hub_deployments

    @create_git_hub_deployments.setter
    def create_git_hub_deployments(self, create_git_hub_deployments):
        """Sets the create_git_hub_deployments of this RepositoryUpdateRequest.

        If GitHub deployments should be created. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser, Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken, and Tgstation.Server.Api.Models.Internal.RepositorySettings.PushTestMergeCommits to be set to function.  # noqa: E501

        :param create_git_hub_deployments: The create_git_hub_deployments of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._create_git_hub_deployments = create_git_hub_deployments

    @property
    def show_test_merge_committers(self):
        """Gets the show_test_merge_committers of this RepositoryUpdateRequest.  # noqa: E501

        If test merge commits are signed with the username of the person who merged it. Note this only affects future commits  # noqa: E501

        :return: The show_test_merge_committers of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._show_test_merge_committers

    @show_test_merge_committers.setter
    def show_test_merge_committers(self, show_test_merge_committers):
        """Sets the show_test_merge_committers of this RepositoryUpdateRequest.

        If test merge commits are signed with the username of the person who merged it. Note this only affects future commits  # noqa: E501

        :param show_test_merge_committers: The show_test_merge_committers of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._show_test_merge_committers = show_test_merge_committers

    @property
    def auto_updates_keep_test_merges(self):
        """Gets the auto_updates_keep_test_merges of this RepositoryUpdateRequest.  # noqa: E501

        If test merge commits should be kept when auto updating. May cause merge conflicts which will block the update  # noqa: E501

        :return: The auto_updates_keep_test_merges of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_updates_keep_test_merges

    @auto_updates_keep_test_merges.setter
    def auto_updates_keep_test_merges(self, auto_updates_keep_test_merges):
        """Sets the auto_updates_keep_test_merges of this RepositoryUpdateRequest.

        If test merge commits should be kept when auto updating. May cause merge conflicts which will block the update  # noqa: E501

        :param auto_updates_keep_test_merges: The auto_updates_keep_test_merges of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._auto_updates_keep_test_merges = auto_updates_keep_test_merges

    @property
    def auto_updates_synchronize(self):
        """Gets the auto_updates_synchronize of this RepositoryUpdateRequest.  # noqa: E501

        If synchronization should occur when auto updating. Requries Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The auto_updates_synchronize of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._auto_updates_synchronize

    @auto_updates_synchronize.setter
    def auto_updates_synchronize(self, auto_updates_synchronize):
        """Sets the auto_updates_synchronize of this RepositoryUpdateRequest.

        If synchronization should occur when auto updating. Requries Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param auto_updates_synchronize: The auto_updates_synchronize of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._auto_updates_synchronize = auto_updates_synchronize

    @property
    def post_test_merge_comment(self):
        """Gets the post_test_merge_comment of this RepositoryUpdateRequest.  # noqa: E501

        If test merging should create a comment. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The post_test_merge_comment of this RepositoryUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._post_test_merge_comment

    @post_test_merge_comment.setter
    def post_test_merge_comment(self, post_test_merge_comment):
        """Sets the post_test_merge_comment of this RepositoryUpdateRequest.

        If test merging should create a comment. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param post_test_merge_comment: The post_test_merge_comment of this RepositoryUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._post_test_merge_comment = post_test_merge_comment

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
        if issubclass(RepositoryUpdateRequest, dict):
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
        if not isinstance(other, RepositoryUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
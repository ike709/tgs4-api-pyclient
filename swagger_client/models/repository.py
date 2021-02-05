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

class Repository(object):
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
        'origin': 'str',
        'recurse_submodules': 'bool',
        'checkout_sha': 'str',
        'revision_information': 'AllOfRepositoryRevisionInformation',
        'remote_git_provider': 'AllOfRepositoryRemoteGitProvider',
        'remote_repository_owner': 'str',
        'remote_repository_name': 'str',
        'active_job': 'AllOfRepositoryActiveJob',
        'update_from_origin': 'bool',
        'reference': 'str',
        'new_test_merges': 'list[TestMergeParameters]',
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
        'origin': 'origin',
        'recurse_submodules': 'recurseSubmodules',
        'checkout_sha': 'checkoutSha',
        'revision_information': 'revisionInformation',
        'remote_git_provider': 'remoteGitProvider',
        'remote_repository_owner': 'remoteRepositoryOwner',
        'remote_repository_name': 'remoteRepositoryName',
        'active_job': 'activeJob',
        'update_from_origin': 'updateFromOrigin',
        'reference': 'reference',
        'new_test_merges': 'newTestMerges',
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

    def __init__(self, origin=None, recurse_submodules=None, checkout_sha=None, revision_information=None, remote_git_provider=None, remote_repository_owner=None, remote_repository_name=None, active_job=None, update_from_origin=None, reference=None, new_test_merges=None, committer_name=None, committer_email=None, access_user=None, access_token=None, push_test_merge_commits=None, create_git_hub_deployments=None, show_test_merge_committers=None, auto_updates_keep_test_merges=None, auto_updates_synchronize=None, post_test_merge_comment=None):  # noqa: E501
        """Repository - a model defined in Swagger"""  # noqa: E501
        self._origin = None
        self._recurse_submodules = None
        self._checkout_sha = None
        self._revision_information = None
        self._remote_git_provider = None
        self._remote_repository_owner = None
        self._remote_repository_name = None
        self._active_job = None
        self._update_from_origin = None
        self._reference = None
        self._new_test_merges = None
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
        if origin is not None:
            self.origin = origin
        if recurse_submodules is not None:
            self.recurse_submodules = recurse_submodules
        if checkout_sha is not None:
            self.checkout_sha = checkout_sha
        if revision_information is not None:
            self.revision_information = revision_information
        if remote_git_provider is not None:
            self.remote_git_provider = remote_git_provider
        if remote_repository_owner is not None:
            self.remote_repository_owner = remote_repository_owner
        if remote_repository_name is not None:
            self.remote_repository_name = remote_repository_name
        if active_job is not None:
            self.active_job = active_job
        if update_from_origin is not None:
            self.update_from_origin = update_from_origin
        if reference is not None:
            self.reference = reference
        if new_test_merges is not None:
            self.new_test_merges = new_test_merges
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
    def origin(self):
        """Gets the origin of this Repository.  # noqa: E501

        The origin URL. If <see langword=\"null\" />, the Tgstation.Server.Api.Models.Repository does not exist  # noqa: E501

        :return: The origin of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this Repository.

        The origin URL. If <see langword=\"null\" />, the Tgstation.Server.Api.Models.Repository does not exist  # noqa: E501

        :param origin: The origin of this Repository.  # noqa: E501
        :type: str
        """

        self._origin = origin

    @property
    def recurse_submodules(self):
        """Gets the recurse_submodules of this Repository.  # noqa: E501

        If submodules should be recursively cloned.  # noqa: E501

        :return: The recurse_submodules of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._recurse_submodules

    @recurse_submodules.setter
    def recurse_submodules(self, recurse_submodules):
        """Sets the recurse_submodules of this Repository.

        If submodules should be recursively cloned.  # noqa: E501

        :param recurse_submodules: The recurse_submodules of this Repository.  # noqa: E501
        :type: bool
        """

        self._recurse_submodules = recurse_submodules

    @property
    def checkout_sha(self):
        """Gets the checkout_sha of this Repository.  # noqa: E501

        The commit HEAD should point to. Not populated in responses, use Tgstation.Server.Api.Models.Repository.RevisionInformation instead for retrieval  # noqa: E501

        :return: The checkout_sha of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._checkout_sha

    @checkout_sha.setter
    def checkout_sha(self, checkout_sha):
        """Sets the checkout_sha of this Repository.

        The commit HEAD should point to. Not populated in responses, use Tgstation.Server.Api.Models.Repository.RevisionInformation instead for retrieval  # noqa: E501

        :param checkout_sha: The checkout_sha of this Repository.  # noqa: E501
        :type: str
        """

        self._checkout_sha = checkout_sha

    @property
    def revision_information(self):
        """Gets the revision_information of this Repository.  # noqa: E501

        The current Tgstation.Server.Api.Models.RevisionInformation for the Tgstation.Server.Api.Models.Repository  # noqa: E501

        :return: The revision_information of this Repository.  # noqa: E501
        :rtype: AllOfRepositoryRevisionInformation
        """
        return self._revision_information

    @revision_information.setter
    def revision_information(self, revision_information):
        """Sets the revision_information of this Repository.

        The current Tgstation.Server.Api.Models.RevisionInformation for the Tgstation.Server.Api.Models.Repository  # noqa: E501

        :param revision_information: The revision_information of this Repository.  # noqa: E501
        :type: AllOfRepositoryRevisionInformation
        """

        self._revision_information = revision_information

    @property
    def remote_git_provider(self):
        """Gets the remote_git_provider of this Repository.  # noqa: E501


        :return: The remote_git_provider of this Repository.  # noqa: E501
        :rtype: AllOfRepositoryRemoteGitProvider
        """
        return self._remote_git_provider

    @remote_git_provider.setter
    def remote_git_provider(self, remote_git_provider):
        """Sets the remote_git_provider of this Repository.


        :param remote_git_provider: The remote_git_provider of this Repository.  # noqa: E501
        :type: AllOfRepositoryRemoteGitProvider
        """

        self._remote_git_provider = remote_git_provider

    @property
    def remote_repository_owner(self):
        """Gets the remote_repository_owner of this Repository.  # noqa: E501


        :return: The remote_repository_owner of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._remote_repository_owner

    @remote_repository_owner.setter
    def remote_repository_owner(self, remote_repository_owner):
        """Sets the remote_repository_owner of this Repository.


        :param remote_repository_owner: The remote_repository_owner of this Repository.  # noqa: E501
        :type: str
        """

        self._remote_repository_owner = remote_repository_owner

    @property
    def remote_repository_name(self):
        """Gets the remote_repository_name of this Repository.  # noqa: E501


        :return: The remote_repository_name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._remote_repository_name

    @remote_repository_name.setter
    def remote_repository_name(self, remote_repository_name):
        """Sets the remote_repository_name of this Repository.


        :param remote_repository_name: The remote_repository_name of this Repository.  # noqa: E501
        :type: str
        """

        self._remote_repository_name = remote_repository_name

    @property
    def active_job(self):
        """Gets the active_job of this Repository.  # noqa: E501

        The Tgstation.Server.Api.Models.Job started by the Tgstation.Server.Api.Models.Repository if any  # noqa: E501

        :return: The active_job of this Repository.  # noqa: E501
        :rtype: AllOfRepositoryActiveJob
        """
        return self._active_job

    @active_job.setter
    def active_job(self, active_job):
        """Sets the active_job of this Repository.

        The Tgstation.Server.Api.Models.Job started by the Tgstation.Server.Api.Models.Repository if any  # noqa: E501

        :param active_job: The active_job of this Repository.  # noqa: E501
        :type: AllOfRepositoryActiveJob
        """

        self._active_job = active_job

    @property
    def update_from_origin(self):
        """Gets the update_from_origin of this Repository.  # noqa: E501

        Do the equivalent of a git pull. Will attempt to merge unless Tgstation.Server.Api.Models.Repository.Reference is also specified in which case a hard reset will be performed after checking out  # noqa: E501

        :return: The update_from_origin of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._update_from_origin

    @update_from_origin.setter
    def update_from_origin(self, update_from_origin):
        """Sets the update_from_origin of this Repository.

        Do the equivalent of a git pull. Will attempt to merge unless Tgstation.Server.Api.Models.Repository.Reference is also specified in which case a hard reset will be performed after checking out  # noqa: E501

        :param update_from_origin: The update_from_origin of this Repository.  # noqa: E501
        :type: bool
        """

        self._update_from_origin = update_from_origin

    @property
    def reference(self):
        """Gets the reference of this Repository.  # noqa: E501

        The branch or tag HEAD points to  # noqa: E501

        :return: The reference of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Repository.

        The branch or tag HEAD points to  # noqa: E501

        :param reference: The reference of this Repository.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def new_test_merges(self):
        """Gets the new_test_merges of this Repository.  # noqa: E501

        Tgstation.Server.Api.Models.TestMergeParameters for new Tgstation.Server.Api.Models.TestMerges. Note that merges that conflict will not be performed  # noqa: E501

        :return: The new_test_merges of this Repository.  # noqa: E501
        :rtype: list[TestMergeParameters]
        """
        return self._new_test_merges

    @new_test_merges.setter
    def new_test_merges(self, new_test_merges):
        """Sets the new_test_merges of this Repository.

        Tgstation.Server.Api.Models.TestMergeParameters for new Tgstation.Server.Api.Models.TestMerges. Note that merges that conflict will not be performed  # noqa: E501

        :param new_test_merges: The new_test_merges of this Repository.  # noqa: E501
        :type: list[TestMergeParameters]
        """

        self._new_test_merges = new_test_merges

    @property
    def committer_name(self):
        """Gets the committer_name of this Repository.  # noqa: E501

        The name of the committer  # noqa: E501

        :return: The committer_name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._committer_name

    @committer_name.setter
    def committer_name(self, committer_name):
        """Sets the committer_name of this Repository.

        The name of the committer  # noqa: E501

        :param committer_name: The committer_name of this Repository.  # noqa: E501
        :type: str
        """

        self._committer_name = committer_name

    @property
    def committer_email(self):
        """Gets the committer_email of this Repository.  # noqa: E501

        The e-mail of the committer  # noqa: E501

        :return: The committer_email of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._committer_email

    @committer_email.setter
    def committer_email(self, committer_email):
        """Sets the committer_email of this Repository.

        The e-mail of the committer  # noqa: E501

        :param committer_email: The committer_email of this Repository.  # noqa: E501
        :type: str
        """

        self._committer_email = committer_email

    @property
    def access_user(self):
        """Gets the access_user of this Repository.  # noqa: E501

        The username to access the git repository with  # noqa: E501

        :return: The access_user of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this Repository.

        The username to access the git repository with  # noqa: E501

        :param access_user: The access_user of this Repository.  # noqa: E501
        :type: str
        """

        self._access_user = access_user

    @property
    def access_token(self):
        """Gets the access_token of this Repository.  # noqa: E501

        The token/password to access the git repository with  # noqa: E501

        :return: The access_token of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this Repository.

        The token/password to access the git repository with  # noqa: E501

        :param access_token: The access_token of this Repository.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

    @property
    def push_test_merge_commits(self):
        """Gets the push_test_merge_commits of this Repository.  # noqa: E501

        If commits created from testmerges are pushed to the remote. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The push_test_merge_commits of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._push_test_merge_commits

    @push_test_merge_commits.setter
    def push_test_merge_commits(self, push_test_merge_commits):
        """Sets the push_test_merge_commits of this Repository.

        If commits created from testmerges are pushed to the remote. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param push_test_merge_commits: The push_test_merge_commits of this Repository.  # noqa: E501
        :type: bool
        """

        self._push_test_merge_commits = push_test_merge_commits

    @property
    def create_git_hub_deployments(self):
        """Gets the create_git_hub_deployments of this Repository.  # noqa: E501

        If GitHub deployments should be created. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser, Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken, and Tgstation.Server.Api.Models.Internal.RepositorySettings.PushTestMergeCommits to be set to function.  # noqa: E501

        :return: The create_git_hub_deployments of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._create_git_hub_deployments

    @create_git_hub_deployments.setter
    def create_git_hub_deployments(self, create_git_hub_deployments):
        """Sets the create_git_hub_deployments of this Repository.

        If GitHub deployments should be created. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser, Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken, and Tgstation.Server.Api.Models.Internal.RepositorySettings.PushTestMergeCommits to be set to function.  # noqa: E501

        :param create_git_hub_deployments: The create_git_hub_deployments of this Repository.  # noqa: E501
        :type: bool
        """

        self._create_git_hub_deployments = create_git_hub_deployments

    @property
    def show_test_merge_committers(self):
        """Gets the show_test_merge_committers of this Repository.  # noqa: E501

        If test merge commits are signed with the username of the person who merged it. Note this only affects future commits  # noqa: E501

        :return: The show_test_merge_committers of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._show_test_merge_committers

    @show_test_merge_committers.setter
    def show_test_merge_committers(self, show_test_merge_committers):
        """Sets the show_test_merge_committers of this Repository.

        If test merge commits are signed with the username of the person who merged it. Note this only affects future commits  # noqa: E501

        :param show_test_merge_committers: The show_test_merge_committers of this Repository.  # noqa: E501
        :type: bool
        """

        self._show_test_merge_committers = show_test_merge_committers

    @property
    def auto_updates_keep_test_merges(self):
        """Gets the auto_updates_keep_test_merges of this Repository.  # noqa: E501

        If test merge commits should be kept when auto updating. May cause merge conflicts which will block the update  # noqa: E501

        :return: The auto_updates_keep_test_merges of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._auto_updates_keep_test_merges

    @auto_updates_keep_test_merges.setter
    def auto_updates_keep_test_merges(self, auto_updates_keep_test_merges):
        """Sets the auto_updates_keep_test_merges of this Repository.

        If test merge commits should be kept when auto updating. May cause merge conflicts which will block the update  # noqa: E501

        :param auto_updates_keep_test_merges: The auto_updates_keep_test_merges of this Repository.  # noqa: E501
        :type: bool
        """

        self._auto_updates_keep_test_merges = auto_updates_keep_test_merges

    @property
    def auto_updates_synchronize(self):
        """Gets the auto_updates_synchronize of this Repository.  # noqa: E501

        If synchronization should occur when auto updating. Requries Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The auto_updates_synchronize of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._auto_updates_synchronize

    @auto_updates_synchronize.setter
    def auto_updates_synchronize(self, auto_updates_synchronize):
        """Sets the auto_updates_synchronize of this Repository.

        If synchronization should occur when auto updating. Requries Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param auto_updates_synchronize: The auto_updates_synchronize of this Repository.  # noqa: E501
        :type: bool
        """

        self._auto_updates_synchronize = auto_updates_synchronize

    @property
    def post_test_merge_comment(self):
        """Gets the post_test_merge_comment of this Repository.  # noqa: E501

        If test merging should create a comment. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :return: The post_test_merge_comment of this Repository.  # noqa: E501
        :rtype: bool
        """
        return self._post_test_merge_comment

    @post_test_merge_comment.setter
    def post_test_merge_comment(self, post_test_merge_comment):
        """Sets the post_test_merge_comment of this Repository.

        If test merging should create a comment. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function.  # noqa: E501

        :param post_test_merge_comment: The post_test_merge_comment of this Repository.  # noqa: E501
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
        if issubclass(Repository, dict):
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
        if not isinstance(other, Repository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
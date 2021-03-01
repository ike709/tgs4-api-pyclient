# RepositoryUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_sha** | **str** | The commit HEAD should point to. | [optional] 
**update_from_origin** | **bool** | Do the equivalent of a git pull. Will attempt to merge unless Tgstation.Server.Api.Models.Internal.RepositoryApiBase.Reference is also specified in which case a hard reset will be performed after checking out | [optional] 
**new_test_merges** | [**list[TestMergeParameters]**](TestMergeParameters.md) | Tgstation.Server.Api.Models.TestMergeParameters for new Tgstation.Server.Api.Models.TestMerges. Note that merges that conflict will not be performed | [optional] 
**reference** | **str** | The branch or tag HEAD points to. | [optional] 
**committer_name** | **str** | The name of the committer | [optional] 
**committer_email** | **str** | The e-mail of the committer | [optional] 
**access_user** | **str** | The username to access the git repository with | [optional] 
**access_token** | **str** | The token/password to access the git repository with | [optional] 
**push_test_merge_commits** | **bool** | If commits created from testmerges are pushed to the remote. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function. | [optional] 
**create_git_hub_deployments** | **bool** | If GitHub deployments should be created. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser, Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken, and Tgstation.Server.Api.Models.Internal.RepositorySettings.PushTestMergeCommits to be set to function. | [optional] 
**show_test_merge_committers** | **bool** | If test merge commits are signed with the username of the person who merged it. Note this only affects future commits | [optional] 
**auto_updates_keep_test_merges** | **bool** | If test merge commits should be kept when auto updating. May cause merge conflicts which will block the update | [optional] 
**auto_updates_synchronize** | **bool** | If synchronization should occur when auto updating. Requries Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessUser and Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function. | [optional] 
**post_test_merge_comment** | **bool** | If test merging should create a comment. Requires Tgstation.Server.Api.Models.Internal.RepositorySettings.AccessToken to be set to function. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


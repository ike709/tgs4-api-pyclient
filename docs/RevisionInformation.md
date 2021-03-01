# RevisionInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_test_merge** | [**AllOfRevisionInformationPrimaryTestMerge**](AllOfRevisionInformationPrimaryTestMerge.md) | The Tgstation.Server.Api.Models.TestMerge that was created with this Tgstation.Server.Api.Models.RevisionInformation | [optional] 
**active_test_merges** | [**list[TestMerge]**](TestMerge.md) | The Tgstation.Server.Api.Models.TestMerges active in the Tgstation.Server.Api.Models.RevisionInformation | [optional] 
**compile_jobs** | [**list[EntityId]**](EntityId.md) | The Tgstation.Server.Api.Models.Internal.CompileJobs made from the Tgstation.Server.Api.Models.RevisionInformation | [optional] 
**commit_sha** | **str** | The revision SHA. | [optional] 
**timestamp** | **datetime** | The timestamp of the revision. | [optional] 
**origin_commit_sha** | **str** | The SHA of the most recent remote commit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


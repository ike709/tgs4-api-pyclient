# TestMerge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged_by** | [**AllOfTestMergeMergedBy**](AllOfTestMergeMergedBy.md) | The Tgstation.Server.Api.Models.NamedEntity of the user who created the Tgstation.Server.Api.Models.TestMerge. | [optional] 
**id** | **int** | The ID of the Tgstation.Server.Api.Models.Internal.TestMergeApiBase | [optional] 
**merged_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.TestMergeApiBase was created | [optional] 
**title_at_merge** | **str** | The title of the test merge source. | [optional] 
**body_at_merge** | **str** | The body of the test merge source. | [optional] 
**url** | **str** | The URL of the test merge source. | [optional] 
**author** | **str** | The author of the test merge source. | [optional] 
**number** | **int** | The number of the test merge source. | [optional] 
**target_commit_sha** | **str** | The sha of the test merge revision to merge. If not specified, the latest commit shall be used (semi-unsafe) | [optional] 
**comment** | **str** | Optional comment about the test | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


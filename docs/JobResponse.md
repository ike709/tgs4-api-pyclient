# JobResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_by** | [**AllOfJobResponseStartedBy**](AllOfJobResponseStartedBy.md) | The Tgstation.Server.Api.Models.Response.UserResponse that started the job | [optional] 
**cancelled_by** | [**AllOfJobResponseCancelledBy**](AllOfJobResponseCancelledBy.md) | The Tgstation.Server.Api.Models.Response.UserResponse that cancelled the job | [optional] 
**progress** | **int** | Optional progress between 0 and 100 inclusive | [optional] 
**description** | **str** | English description of the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**error_code** | [**AllOfJobResponseErrorCode**](AllOfJobResponseErrorCode.md) | The Tgstation.Server.Api.Models.ErrorCode associated with the Tgstation.Server.Api.Models.Internal.Job if any. | [optional] 
**exception_details** | **str** | Details of any exceptions caught during the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**started_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.Job was started | [optional] 
**stopped_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.Job stopped | [optional] 
**cancelled** | **bool** | If the Tgstation.Server.Api.Models.Internal.Job was cancelled | [optional] 
**cancel_rights_type** | [**AllOfJobResponseCancelRightsType**](AllOfJobResponseCancelRightsType.md) | The Tgstation.Server.Api.Rights.RightsType of Tgstation.Server.Api.Models.Internal.Job.CancelRight if it can be cancelled | [optional] 
**cancel_right** | **int** | The N:Tgstation.Server.Api.Rights required to cancel the Tgstation.Server.Api.Models.Internal.Job | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


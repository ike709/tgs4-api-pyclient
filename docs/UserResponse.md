# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**AllOfUserResponseCreatedBy**](AllOfUserResponseCreatedBy.md) | The Tgstation.Server.Api.Models.Response.UserResponse who created this Tgstation.Server.Api.Models.Response.UserResponse | [optional] 
**o_auth_connections** | [**list[OAuthConnection]**](OAuthConnection.md) | List of Tgstation.Server.Api.Models.OAuthConnections associated with the user. | [optional] 
**permission_set** | [**AllOfUserResponsePermissionSet**](AllOfUserResponsePermissionSet.md) | The Tgstation.Server.Api.Models.PermissionSet directly associated with the user. | [optional] 
**group** | [**AllOfUserResponseGroup**](AllOfUserResponseGroup.md) | The Tgstation.Server.Api.Models.Internal.UserGroup asociated with the user, if any. | [optional] 
**enabled** | **bool** | If the Tgstation.Server.Api.Models.Internal.UserModelBase is enabled since users cannot be deleted. System users cannot be disabled | [optional] 
**created_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.UserModelBase was created | [optional] 
**system_identifier** | **str** | The SID/UID of the Tgstation.Server.Api.Models.Internal.UserModelBase on Windows/POSIX respectively | [optional] 
**name** | **str** |  | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


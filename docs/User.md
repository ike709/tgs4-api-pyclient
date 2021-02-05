# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | [**AllOfUserCreatedBy**](AllOfUserCreatedBy.md) | The Tgstation.Server.Api.Models.User who created this Tgstation.Server.Api.Models.User | [optional] 
**o_auth_connections** | [**list[OAuthConnection]**](OAuthConnection.md) | List of Tgstation.Server.Api.Models.OAuthConnections associated with the Tgstation.Server.Api.Models.User. | [optional] 
**permission_set** | [**AllOfUserPermissionSet**](AllOfUserPermissionSet.md) | The Tgstation.Server.Api.Models.PermissionSet directly associated with the Tgstation.Server.Api.Models.User. | [optional] 
**group** | [**AllOfUserGroup**](AllOfUserGroup.md) | The Tgstation.Server.Api.Models.Internal.UserGroup asociated with the Tgstation.Server.Api.Models.User, if any. | [optional] 
**enabled** | **bool** | If the Tgstation.Server.Api.Models.Internal.User is enabled since users cannot be deleted. System users cannot be disabled | [optional] 
**created_at** | **datetime** | When the Tgstation.Server.Api.Models.Internal.User was created | [optional] 
**system_identifier** | **str** | The SID/UID of the Tgstation.Server.Api.Models.Internal.User on Windows/POSIX respectively | [optional] 
**id** | **int** | The ID of the Tgstation.Server.Api.Models.Internal.User | [optional] 
**name** | **str** | The name of the Tgstation.Server.Api.Models.Internal.User | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


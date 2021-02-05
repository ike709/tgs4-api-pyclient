# Instance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Tgstation.Server.Api.Models.Instance | [optional] 
**path** | **str** | The path to where the Tgstation.Server.Api.Models.Instance is located. Can only be changed while the Tgstation.Server.Api.Models.Instance is offline. Must not exist when the instance is created | [optional] 
**online** | **bool** | If the Tgstation.Server.Api.Models.Instance is online | [optional] 
**configuration_type** | [**AllOfInstanceConfigurationType**](AllOfInstanceConfigurationType.md) | If Tgstation.Server.Api.Models.ConfigurationFile can be used on the Tgstation.Server.Api.Models.Instance | [optional] 
**auto_update_interval** | **int** | The time interval in minutes the repository is automatically pulled and compiles. 0 disables | [optional] 
**chat_bot_limit** | **int** | The maximum number of Tgstation.Server.Api.Models.ChatBots the Tgstation.Server.Api.Models.Instance may contain. | [optional] 
**move_job** | [**AllOfInstanceMoveJob**](AllOfInstanceMoveJob.md) | The Tgstation.Server.Api.Models.Job representing a change of Tgstation.Server.Api.Models.Instance.Path | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


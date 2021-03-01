# InstanceCreateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The path to where the Tgstation.Server.Api.Models.Instance is located. Can only be changed while the Tgstation.Server.Api.Models.Instance is offline. Must not exist when the instance is created | [optional] 
**configuration_type** | [**AllOfInstanceCreateRequestConfigurationType**](AllOfInstanceCreateRequestConfigurationType.md) | If Tgstation.Server.Api.Models.IConfigurationFiles can be used on the Tgstation.Server.Api.Models.Instance | [optional] 
**auto_update_interval** | **int** | The time interval in minutes the repository is automatically pulled and compiles. 0 disables | [optional] 
**chat_bot_limit** | **int** | The maximum number of chat bots the Tgstation.Server.Api.Models.Instance may contain. | [optional] 
**name** | **str** | The name of the entity represented by the Tgstation.Server.Api.Models.NamedEntity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ChatBot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**list[ChatChannel]**](ChatChannel.md) | Channels the Discord bot should listen/announce in | [optional] 
**name** | **str** | The name of the connection | [optional] 
**enabled** | **bool** | If the connection is enabled | [optional] 
**reconnection_interval** | **int** | The time interval in minutes the chat bot attempts to reconnect if Tgstation.Server.Api.Models.Internal.ChatBot.Enabled and disconnected. Must not be zero. | [optional] 
**channel_limit** | **int** | The maximum number of Tgstation.Server.Api.Models.ChatChannels the Tgstation.Server.Api.Models.Internal.ChatBot may contain. | [optional] 
**provider** | [**AllOfChatBotProvider**](AllOfChatBotProvider.md) | The Tgstation.Server.Api.Models.ChatProvider used for the connection | [optional] 
**connection_string** | **str** | The information used to connect to the Tgstation.Server.Api.Models.Internal.ChatBot.Provider | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


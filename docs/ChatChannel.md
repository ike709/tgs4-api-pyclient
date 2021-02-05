# ChatChannel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**irc_channel** | **str** | The IRC channel name. Also potentially contains the channel passsword (if separated by a colon). If multiple copies of the same channel with different keys are added to the server, the one that will be used is undefined. | [optional] 
**discord_channel_id** | **int** | The Discord channel ID | [optional] 
**is_admin_channel** | **bool** | If the Tgstation.Server.Api.Models.ChatChannel is an admin channel | [optional] 
**is_watchdog_channel** | **bool** | If the Tgstation.Server.Api.Models.ChatChannel is a watchdog channel | [optional] 
**is_updates_channel** | **bool** | If the Tgstation.Server.Api.Models.ChatChannel is an updates channel | [optional] 
**tag** | **str** | A custom tag users can define to group channels together | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


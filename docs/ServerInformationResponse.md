# ServerInformationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the host | [optional] 
**api_version** | **str** | The N:Tgstation.Server.Api version of the host | [optional] 
**dm_api_version** | **str** | The DMAPI interop version the server uses. | [optional] 
**windows_host** | **bool** | If the server is running on a windows operating system. | [optional] 
**update_in_progress** | **bool** | If there is a server update in progress. | [optional] 
**swarm_servers** | [**list[SwarmServerResponse]**](SwarmServerResponse.md) | A System.Collections.Generic.ICollection&#x60;1 of connected Tgstation.Server.Api.Models.Response.SwarmServerResponses. | [optional] 
**o_auth_provider_infos** | [**ServerInformationResponseOAuthProviderInfos**](ServerInformationResponseOAuthProviderInfos.md) |  | [optional] 
**minimum_password_length** | **int** | Minimum length of database user passwords. | [optional] 
**instance_limit** | **int** | The maximum number of Tgstation.Server.Api.Models.Instances allowed. | [optional] 
**user_limit** | **int** | The maximum number of users allowed. | [optional] 
**user_group_limit** | **int** | The maximum number of user groups allowed. | [optional] 
**valid_instance_paths** | **list[str]** | Limits the locations instances may be created or attached from. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


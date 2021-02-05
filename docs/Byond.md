# Byond

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The System.Version of the Tgstation.Server.Api.Models.Byond installation used for new compiles. Will be &lt;see langword&#x3D;\&quot;null\&quot; /&gt; if the user does not have permission to view it or there is no BYOND version installed. Only considers the System.Version.Major and System.Version.Minor numbers. | [optional] 
**install_job** | [**AllOfByondInstallJob**](AllOfByondInstallJob.md) | The Tgstation.Server.Api.Models.Job being used to install a new Tgstation.Server.Api.Models.Byond.Version | [optional] 
**upload_custom_zip** | **bool** | If a custom BYOND version is to be uploaded. | [optional] 
**file_ticket** | **str** | The ticket to use to access the Tgstation.Server.Api.Routes.Transfer controller. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# CompileJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**AllOfCompileJobJob**](AllOfCompileJobJob.md) | The Tgstation.Server.Api.Models.CompileJob.Job relating to this job | [optional] 
**revision_information** | [**AllOfCompileJobRevisionInformation**](AllOfCompileJobRevisionInformation.md) | Git revision the compiler ran on. Not modifiable | [optional] 
**byond_version** | **str** | The Tgstation.Server.Api.Models.Byond.Version the Tgstation.Server.Api.Models.CompileJob was made with | [optional] 
**repository_origin** | **str** | The origin System.Uri of the repository the compile job was built from. | [optional] 
**dme_name** | **str** | The .dme file used for compilation | [optional] 
**output** | **str** | Textual output of DM | [optional] 
**directory_name** | **str** | The Game folder the results were compiled into | [optional] 
**minimum_security_level** | [**AllOfCompileJobMinimumSecurityLevel**](AllOfCompileJobMinimumSecurityLevel.md) | The minimum Tgstation.Server.Api.Models.DreamDaemonSecurity required to run the Tgstation.Server.Api.Models.Internal.CompileJob&#x27;s output | [optional] 
**dm_api_version** | **str** | The DMAPI System.Version. | [optional] 
**id** | **int** | The ID of the entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


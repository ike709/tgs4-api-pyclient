# DreamDaemonResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_compile_job** | [**AllOfDreamDaemonResponseActiveCompileJob**](AllOfDreamDaemonResponseActiveCompileJob.md) | The live revision. | [optional] 
**staged_compile_job** | [**AllOfDreamDaemonResponseStagedCompileJob**](AllOfDreamDaemonResponseStagedCompileJob.md) | The next revision to go live. | [optional] 
**status** | [**AllOfDreamDaemonResponseStatus**](AllOfDreamDaemonResponseStatus.md) | The current Tgstation.Server.Api.Models.WatchdogStatus. | [optional] 
**current_security** | [**AllOfDreamDaemonResponseCurrentSecurity**](AllOfDreamDaemonResponseCurrentSecurity.md) | The current Tgstation.Server.Api.Models.DreamDaemonSecurity of Tgstation.Server.Api.Models.Response.DreamDaemonResponse. May be downgraded due to requirements of Tgstation.Server.Api.Models.Response.DreamDaemonResponse.ActiveCompileJob | [optional] 
**current_port** | **int** | The port the running Tgstation.Server.Api.Models.Response.DreamDaemonResponse instance is set to | [optional] 
**current_allow_webclient** | **bool** | The webclient status the running Tgstation.Server.Api.Models.Response.DreamDaemonResponse instance is set to | [optional] 
**soft_restart** | **bool** | If the server is undergoing a soft reset. This may be automatically set by changes to other fields | [optional] 
**soft_shutdown** | **bool** | If the server is undergoing a soft shutdown | [optional] 
**auto_start** | **bool** | If the watchdog starts when it&#x27;s Tgstation.Server.Api.Models.Instance starts | [optional] 
**allow_web_client** | **bool** | If the BYOND web client can be used to connect to the game server | [optional] 
**security_level** | [**AllOfDreamDaemonResponseSecurityLevel**](AllOfDreamDaemonResponseSecurityLevel.md) | The Tgstation.Server.Api.Models.DreamDaemonSecurity level of DreamDaemon. | [optional] 
**port** | **int** | The port DreamDaemon uses. This should be publically accessible. | [optional] 
**startup_timeout** | **int** | The DreamDaemon startup timeout in seconds | [optional] 
**heartbeat_seconds** | **int** | The number of seconds between each watchdog heartbeat. 0 disables. | [optional] 
**topic_request_timeout** | **int** | The timeout for sending and receiving BYOND topics in milliseconds. | [optional] 
**additional_parameters** | **str** | Parameters string for DreamDaemon. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# DreamDaemon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_compile_job** | [**AllOfDreamDaemonActiveCompileJob**](AllOfDreamDaemonActiveCompileJob.md) | The live revision | [optional] 
**staged_compile_job** | [**AllOfDreamDaemonStagedCompileJob**](AllOfDreamDaemonStagedCompileJob.md) | The next revision to go live | [optional] 
**status** | [**AllOfDreamDaemonStatus**](AllOfDreamDaemonStatus.md) | The current Tgstation.Server.Api.Models.WatchdogStatus. | [optional] 
**current_security** | [**AllOfDreamDaemonCurrentSecurity**](AllOfDreamDaemonCurrentSecurity.md) | The current Tgstation.Server.Api.Models.DreamDaemonSecurity of Tgstation.Server.Api.Models.DreamDaemon. May be downgraded due to requirements of Tgstation.Server.Api.Models.DreamDaemon.ActiveCompileJob | [optional] 
**current_port** | **int** | The port the running Tgstation.Server.Api.Models.DreamDaemon instance is set to | [optional] 
**current_allow_webclient** | **bool** | The webclient status the running Tgstation.Server.Api.Models.DreamDaemon instance is set to | [optional] 
**soft_restart** | **bool** | If the server is undergoing a soft reset. This may be automatically set by changes to other fields | [optional] 
**soft_shutdown** | **bool** | If the server is undergoing a soft shutdown | [optional] 
**create_dump** | **bool** | If a dump of the active DreamDaemon executable should be created. | [optional] 
**auto_start** | **bool** | If Tgstation.Server.Api.Models.DreamDaemon starts when it&#x27;s Tgstation.Server.Api.Models.Instance starts | [optional] 
**allow_web_client** | **bool** | If the BYOND web client can be used to connect to the game server | [optional] 
**security_level** | [**AllOfDreamDaemonSecurityLevel**](AllOfDreamDaemonSecurityLevel.md) | The Tgstation.Server.Api.Models.DreamDaemonSecurity level of Tgstation.Server.Api.Models.DreamDaemon | [optional] 
**port** | **int** | The first port Tgstation.Server.Api.Models.DreamDaemon uses. This should be the publically advertised port | [optional] 
**startup_timeout** | **int** | The DreamDaemon startup timeout in seconds | [optional] 
**heartbeat_seconds** | **int** | The number of seconds between each watchdog heartbeat. 0 disables. | [optional] 
**topic_request_timeout** | **int** | The timeout for sending and receiving BYOND topics in milliseconds. | [optional] 
**additional_parameters** | **str** | Parameters string for DreamDaemon. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


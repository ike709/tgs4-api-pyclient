# swagger_client.DreamDaemonApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dream_daemon_controller_create**](DreamDaemonApi.md#dream_daemon_controller_create) | **PUT** /DreamDaemon | Launches the watchdog.
[**dream_daemon_controller_create_dump**](DreamDaemonApi.md#dream_daemon_controller_create_dump) | **PATCH** /DreamDaemon/Diagnostics | Creates a Tgstation.Server.Api.Models.Response.JobResponse to generate a DreamDaemon process dump.
[**dream_daemon_controller_delete**](DreamDaemonApi.md#dream_daemon_controller_delete) | **DELETE** /DreamDaemon | Stops the Watchdog if it&#x27;s running.
[**dream_daemon_controller_read**](DreamDaemonApi.md#dream_daemon_controller_read) | **GET** /DreamDaemon | Get the watchdog status.
[**dream_daemon_controller_restart**](DreamDaemonApi.md#dream_daemon_controller_restart) | **PATCH** /DreamDaemon | Creates a Tgstation.Server.Api.Models.Response.JobResponse to restart the Watchdog. It will not start if it wasn&#x27;t already running.
[**dream_daemon_controller_update**](DreamDaemonApi.md#dream_daemon_controller_update) | **POST** /DreamDaemon | Update watchdog settings to be applied at next server reboot.

# **dream_daemon_controller_create**
> JobResponse dream_daemon_controller_create(api, user_agent, instance)

Launches the watchdog.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Launches the watchdog.
    api_response = api_instance.dream_daemon_controller_create(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_create_dump**
> JobResponse dream_daemon_controller_create_dump(api, user_agent, instance)

Creates a Tgstation.Server.Api.Models.Response.JobResponse to generate a DreamDaemon process dump.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Creates a Tgstation.Server.Api.Models.Response.JobResponse to generate a DreamDaemon process dump.
    api_response = api_instance.dream_daemon_controller_create_dump(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_create_dump: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_delete**
> dream_daemon_controller_delete(api, user_agent, instance)

Stops the Watchdog if it's running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Stops the Watchdog if it's running.
    api_instance.dream_daemon_controller_delete(api, user_agent, instance)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_read**
> DreamDaemonResponse dream_daemon_controller_read(api, user_agent, instance)

Get the watchdog status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Get the watchdog status.
    api_response = api_instance.dream_daemon_controller_read(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**DreamDaemonResponse**](DreamDaemonResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_restart**
> JobResponse dream_daemon_controller_restart(api, user_agent, instance)

Creates a Tgstation.Server.Api.Models.Response.JobResponse to restart the Watchdog. It will not start if it wasn't already running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Creates a Tgstation.Server.Api.Models.Response.JobResponse to restart the Watchdog. It will not start if it wasn't already running.
    api_response = api_instance.dream_daemon_controller_restart(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_daemon_controller_update**
> DreamDaemonResponse dream_daemon_controller_update(body, api, user_agent, instance)

Update watchdog settings to be applied at next server reboot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamDaemonApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body28() # Body28 | The updated Tgstation.Server.Api.Models.Response.DreamDaemonResponse settings.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Update watchdog settings to be applied at next server reboot.
    api_response = api_instance.dream_daemon_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamDaemonApi->dream_daemon_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body28**](Body28.md)| The updated Tgstation.Server.Api.Models.Response.DreamDaemonResponse settings. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**DreamDaemonResponse**](DreamDaemonResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


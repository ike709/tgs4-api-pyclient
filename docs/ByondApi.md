# swagger_client.ByondApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**byond_controller_list**](ByondApi.md#byond_controller_list) | **GET** /Byond/List | Lists installed Tgstation.Server.Api.Models.Response.ByondResponse.Versions.
[**byond_controller_read**](ByondApi.md#byond_controller_read) | **GET** /Byond | Gets the active Tgstation.Server.Api.Models.Response.ByondResponse.Version.
[**byond_controller_update**](ByondApi.md#byond_controller_update) | **POST** /Byond | Changes the active BYOND version to the one specified in a given model.

# **byond_controller_list**
> PaginatedByondResponse byond_controller_list(api, user_agent, instance, page=page, page_size=page_size)

Lists installed Tgstation.Server.Api.Models.Response.ByondResponse.Versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Lists installed Tgstation.Server.Api.Models.Response.ByondResponse.Versions.
    api_response = api_instance.byond_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **page** | **int**| The current page. | [optional] 
 **page_size** | **int**| The page size. | [optional] 

### Return type

[**PaginatedByondResponse**](PaginatedByondResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **byond_controller_read**
> ByondResponse byond_controller_read(api, user_agent, instance)

Gets the active Tgstation.Server.Api.Models.Response.ByondResponse.Version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Gets the active Tgstation.Server.Api.Models.Response.ByondResponse.Version.
    api_response = api_instance.byond_controller_read(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**ByondResponse**](ByondResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **byond_controller_update**
> ByondInstallResponse byond_controller_update(body, api, user_agent, instance)

Changes the active BYOND version to the one specified in a given model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ByondApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body4() # Body4 | The Tgstation.Server.Api.Models.Request.ByondVersionRequest.Version to switch to.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Changes the active BYOND version to the one specified in a given model.
    api_response = api_instance.byond_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ByondApi->byond_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)| The Tgstation.Server.Api.Models.Request.ByondVersionRequest.Version to switch to. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**ByondInstallResponse**](ByondInstallResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


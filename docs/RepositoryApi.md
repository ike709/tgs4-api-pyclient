# swagger_client.RepositoryApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_controller_create**](RepositoryApi.md#repository_controller_create) | **PUT** /Repository | Begin cloning the repository if it doesn&#x27;t exist.
[**repository_controller_delete**](RepositoryApi.md#repository_controller_delete) | **DELETE** /Repository | Delete the repository.
[**repository_controller_read**](RepositoryApi.md#repository_controller_read) | **GET** /Repository | Get the repository&#x27;s status.
[**repository_controller_update**](RepositoryApi.md#repository_controller_update) | **POST** /Repository | Perform updates to the repository.

# **repository_controller_create**
> RepositoryResponse repository_controller_create(body, api, user_agent, instance)

Begin cloning the repository if it doesn't exist.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body52() # Body52 | The Tgstation.Server.Api.Models.Request.RepositoryCreateRequest.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Begin cloning the repository if it doesn't exist.
    api_response = api_instance.repository_controller_create(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body52**](Body52.md)| The Tgstation.Server.Api.Models.Request.RepositoryCreateRequest. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_delete**
> RepositoryResponse repository_controller_delete(api, user_agent, instance)

Delete the repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Delete the repository.
    api_response = api_instance.repository_controller_delete(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_read**
> RepositoryResponse repository_controller_read(api, user_agent, instance)

Get the repository's status.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Get the repository's status.
    api_response = api_instance.repository_controller_read(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_update**
> RepositoryResponse repository_controller_update(body, api, user_agent, instance)

Perform updates to the repository.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RepositoryApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body56() # Body56 | The Tgstation.Server.Api.Models.Request.RepositoryUpdateRequest.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Perform updates to the repository.
    api_response = api_instance.repository_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body56**](Body56.md)| The Tgstation.Server.Api.Models.Request.RepositoryUpdateRequest. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.RepositoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repository_controller_create**](RepositoryApi.md#repository_controller_create) | **PUT** /Repository | Begin cloning the repository if it doesn&#x27;t exist.
[**repository_controller_delete**](RepositoryApi.md#repository_controller_delete) | **DELETE** /Repository | Delete the Tgstation.Server.Api.Models.Repository.
[**repository_controller_read**](RepositoryApi.md#repository_controller_read) | **GET** /Repository | Get Tgstation.Server.Api.Models.Repository status.
[**repository_controller_update**](RepositoryApi.md#repository_controller_update) | **POST** /Repository | Perform updats to the Tgstation.Server.Api.Models.Repository.

# **repository_controller_create**
> Repository repository_controller_create(api, user_agent, instance, body=body)

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
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
body = swagger_client.Body52() # Body52 | Initial Tgstation.Server.Api.Models.Repository settings. (optional)

try:
    # Begin cloning the repository if it doesn't exist.
    api_response = api_instance.repository_controller_create(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body52**](Body52.md)| Initial Tgstation.Server.Api.Models.Repository settings. | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_delete**
> Repository repository_controller_delete(api, user_agent, instance)

Delete the Tgstation.Server.Api.Models.Repository.

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
    # Delete the Tgstation.Server.Api.Models.Repository.
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

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_read**
> Repository repository_controller_read(api, user_agent, instance)

Get Tgstation.Server.Api.Models.Repository status.

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
    # Get Tgstation.Server.Api.Models.Repository status.
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

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repository_controller_update**
> Repository repository_controller_update(api, user_agent, instance, body=body)

Perform updats to the Tgstation.Server.Api.Models.Repository.

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
body = swagger_client.Body56() # Body56 | The updated Tgstation.Server.Api.Models.Repository. (optional)

try:
    # Perform updats to the Tgstation.Server.Api.Models.Repository.
    api_response = api_instance.repository_controller_update(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepositoryApi->repository_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body56**](Body56.md)| The updated Tgstation.Server.Api.Models.Repository. | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# swagger_client.InstancePermissionSetApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_permission_set_controller_create**](InstancePermissionSetApi.md#instance_permission_set_controller_create) | **PUT** /InstancePermissionSet | Create an Tgstation.Server.Api.Models.InstancePermissionSet.
[**instance_permission_set_controller_delete**](InstancePermissionSetApi.md#instance_permission_set_controller_delete) | **DELETE** /InstancePermissionSet/{id} | Delete an Tgstation.Server.Api.Models.InstancePermissionSet.
[**instance_permission_set_controller_get_id**](InstancePermissionSetApi.md#instance_permission_set_controller_get_id) | **GET** /InstancePermissionSet/{id} | Gets a specific Tgstation.Server.Api.Models.InstancePermissionSet.
[**instance_permission_set_controller_list**](InstancePermissionSetApi.md#instance_permission_set_controller_list) | **GET** /InstancePermissionSet/List | Lists Tgstation.Server.Api.Models.InstancePermissionSets for the instance.
[**instance_permission_set_controller_read**](InstancePermissionSetApi.md#instance_permission_set_controller_read) | **GET** /InstancePermissionSet | Read the active Tgstation.Server.Api.Models.InstancePermissionSet.
[**instance_permission_set_controller_update**](InstancePermissionSetApi.md#instance_permission_set_controller_update) | **POST** /InstancePermissionSet | Update the permissions for an Tgstation.Server.Api.Models.InstancePermissionSet.

# **instance_permission_set_controller_create**
> InstancePermissionSet instance_permission_set_controller_create(api, user_agent, instance, body=body)

Create an Tgstation.Server.Api.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
body = swagger_client.Body44() # Body44 | The Tgstation.Server.Api.Models.InstancePermissionSet to create. (optional)

try:
    # Create an Tgstation.Server.Api.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_create(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body44**](Body44.md)| The Tgstation.Server.Api.Models.InstancePermissionSet to create. | [optional] 

### Return type

[**InstancePermissionSet**](InstancePermissionSet.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_delete**
> instance_permission_set_controller_delete(api, user_agent, instance, id)

Delete an Tgstation.Server.Api.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.InstancePermissionSet.PermissionSetId to delete.

try:
    # Delete an Tgstation.Server.Api.Models.InstancePermissionSet.
    api_instance.instance_permission_set_controller_delete(api, user_agent, instance, id)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.InstancePermissionSet.PermissionSetId to delete. | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_get_id**
> InstancePermissionSet instance_permission_set_controller_get_id(api, user_agent, instance, id)

Gets a specific Tgstation.Server.Api.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.InstancePermissionSet.PermissionSetId.

try:
    # Gets a specific Tgstation.Server.Api.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_get_id(api, user_agent, instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.InstancePermissionSet.PermissionSetId. | 

### Return type

[**InstancePermissionSet**](InstancePermissionSet.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_list**
> PaginatedInstancePermissionSet instance_permission_set_controller_list(api, user_agent, instance, page=page, page_size=page_size)

Lists Tgstation.Server.Api.Models.InstancePermissionSets for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Lists Tgstation.Server.Api.Models.InstancePermissionSets for the instance.
    api_response = api_instance.instance_permission_set_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_list: %s\n" % e)
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

[**PaginatedInstancePermissionSet**](PaginatedInstancePermissionSet.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_read**
> InstancePermissionSet instance_permission_set_controller_read(api, user_agent, instance)

Read the active Tgstation.Server.Api.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Read the active Tgstation.Server.Api.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_read(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**InstancePermissionSet**](InstancePermissionSet.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_update**
> InstancePermissionSet instance_permission_set_controller_update(api, user_agent, instance, body=body)

Update the permissions for an Tgstation.Server.Api.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
body = swagger_client.Body48() # Body48 | The updated Tgstation.Server.Api.Models.InstancePermissionSet. (optional)

try:
    # Update the permissions for an Tgstation.Server.Api.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_update(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body48**](Body48.md)| The updated Tgstation.Server.Api.Models.InstancePermissionSet. | [optional] 

### Return type

[**InstancePermissionSet**](InstancePermissionSet.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


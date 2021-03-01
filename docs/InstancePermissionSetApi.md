# swagger_client.InstancePermissionSetApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_permission_set_controller_create**](InstancePermissionSetApi.md#instance_permission_set_controller_create) | **PUT** /InstancePermissionSet | Create an Tgstation.Server.Host.Models.InstancePermissionSet.
[**instance_permission_set_controller_delete**](InstancePermissionSetApi.md#instance_permission_set_controller_delete) | **DELETE** /InstancePermissionSet/{id} | Delete an Tgstation.Server.Host.Models.InstancePermissionSet.
[**instance_permission_set_controller_get_id**](InstancePermissionSetApi.md#instance_permission_set_controller_get_id) | **GET** /InstancePermissionSet/{id} | Gets a specific Tgstation.Server.Api.Models.Internal.InstancePermissionSet.
[**instance_permission_set_controller_list**](InstancePermissionSetApi.md#instance_permission_set_controller_list) | **GET** /InstancePermissionSet/List | Lists Tgstation.Server.Host.Models.InstancePermissionSets for the instance.
[**instance_permission_set_controller_read**](InstancePermissionSetApi.md#instance_permission_set_controller_read) | **GET** /InstancePermissionSet | Read the active Tgstation.Server.Host.Models.InstancePermissionSet.
[**instance_permission_set_controller_update**](InstancePermissionSetApi.md#instance_permission_set_controller_update) | **POST** /InstancePermissionSet | Update the permissions for an Tgstation.Server.Host.Models.InstancePermissionSet.

# **instance_permission_set_controller_create**
> InstancePermissionSetResponse instance_permission_set_controller_create(body, api, user_agent, instance)

Create an Tgstation.Server.Host.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body44() # Body44 | The Tgstation.Server.Api.Models.Request.InstancePermissionSetRequest.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Create an Tgstation.Server.Host.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_create(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body44**](Body44.md)| The Tgstation.Server.Api.Models.Request.InstancePermissionSetRequest. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**InstancePermissionSetResponse**](InstancePermissionSetResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_delete**
> instance_permission_set_controller_delete(api, user_agent, instance, id)

Delete an Tgstation.Server.Host.Models.InstancePermissionSet.

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
id = 789 # int | The Tgstation.Server.Api.Models.Internal.InstancePermissionSet.PermissionSetId to delete.

try:
    # Delete an Tgstation.Server.Host.Models.InstancePermissionSet.
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
 **id** | **int**| The Tgstation.Server.Api.Models.Internal.InstancePermissionSet.PermissionSetId to delete. | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_get_id**
> InstancePermissionSetResponse instance_permission_set_controller_get_id(api, user_agent, instance, id)

Gets a specific Tgstation.Server.Api.Models.Internal.InstancePermissionSet.

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
id = 789 # int | The Tgstation.Server.Api.Models.Internal.InstancePermissionSet.PermissionSetId.

try:
    # Gets a specific Tgstation.Server.Api.Models.Internal.InstancePermissionSet.
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
 **id** | **int**| The Tgstation.Server.Api.Models.Internal.InstancePermissionSet.PermissionSetId. | 

### Return type

[**InstancePermissionSetResponse**](InstancePermissionSetResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_list**
> PaginatedInstancePermissionSetResponse instance_permission_set_controller_list(api, user_agent, instance, page=page, page_size=page_size)

Lists Tgstation.Server.Host.Models.InstancePermissionSets for the instance.

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
    # Lists Tgstation.Server.Host.Models.InstancePermissionSets for the instance.
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

[**PaginatedInstancePermissionSetResponse**](PaginatedInstancePermissionSetResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_read**
> InstancePermissionSetResponse instance_permission_set_controller_read(api, user_agent, instance)

Read the active Tgstation.Server.Host.Models.InstancePermissionSet.

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
    # Read the active Tgstation.Server.Host.Models.InstancePermissionSet.
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

[**InstancePermissionSetResponse**](InstancePermissionSetResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instance_permission_set_controller_update**
> InstancePermissionSetResponse instance_permission_set_controller_update(body, api, user_agent, instance)

Update the permissions for an Tgstation.Server.Host.Models.InstancePermissionSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.InstancePermissionSetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body48() # Body48 | The Tgstation.Server.Api.Models.Request.InstancePermissionSetRequest.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Update the permissions for an Tgstation.Server.Host.Models.InstancePermissionSet.
    api_response = api_instance.instance_permission_set_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstancePermissionSetApi->instance_permission_set_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body48**](Body48.md)| The Tgstation.Server.Api.Models.Request.InstancePermissionSetRequest. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**InstancePermissionSetResponse**](InstancePermissionSetResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


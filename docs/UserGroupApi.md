# swagger_client.UserGroupApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_group_controller_create**](UserGroupApi.md#user_group_controller_create) | **PUT** /UserGroup | Create a new Tgstation.Server.Api.Models.UserGroup.
[**user_group_controller_delete**](UserGroupApi.md#user_group_controller_delete) | **DELETE** /UserGroup/{id} | Delete an Tgstation.Server.Api.Models.UserGroup.
[**user_group_controller_get_id**](UserGroupApi.md#user_group_controller_get_id) | **GET** /UserGroup/{id} | Gets a specific Tgstation.Server.Api.Models.UserGroup.
[**user_group_controller_list**](UserGroupApi.md#user_group_controller_list) | **GET** /UserGroup/List | Lists all Tgstation.Server.Api.Models.UserGroups.
[**user_group_controller_update**](UserGroupApi.md#user_group_controller_update) | **POST** /UserGroup | Update a Tgstation.Server.Api.Models.UserGroup.

# **user_group_controller_create**
> UserGroup user_group_controller_create(api, user_agent, body=body)

Create a new Tgstation.Server.Api.Models.UserGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserGroupApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Body68() # Body68 | The Tgstation.Server.Api.Models.UserGroup to create. (optional)

try:
    # Create a new Tgstation.Server.Api.Models.UserGroup.
    api_response = api_instance.user_group_controller_create(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Body68**](Body68.md)| The Tgstation.Server.Api.Models.UserGroup to create. | [optional] 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_controller_delete**
> user_group_controller_delete(api, user_agent, id)

Delete an Tgstation.Server.Api.Models.UserGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserGroupApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup to delete.

try:
    # Delete an Tgstation.Server.Api.Models.UserGroup.
    api_instance.user_group_controller_delete(api, user_agent, id)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup to delete. | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_controller_get_id**
> UserGroup user_group_controller_get_id(api, user_agent, id)

Gets a specific Tgstation.Server.Api.Models.UserGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserGroupApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup.

try:
    # Gets a specific Tgstation.Server.Api.Models.UserGroup.
    api_response = api_instance.user_group_controller_get_id(api, user_agent, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.UserGroup. | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_controller_list**
> PaginatedUserGroup user_group_controller_list(api, user_agent, page=page, page_size=page_size)

Lists all Tgstation.Server.Api.Models.UserGroups.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserGroupApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Lists all Tgstation.Server.Api.Models.UserGroups.
    api_response = api_instance.user_group_controller_list(api, user_agent, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_controller_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **page** | **int**| The current page. | [optional] 
 **page_size** | **int**| The page size. | [optional] 

### Return type

[**PaginatedUserGroup**](PaginatedUserGroup.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_group_controller_update**
> UserGroup user_group_controller_update(api, user_agent, body=body)

Update a Tgstation.Server.Api.Models.UserGroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UserGroupApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
body = swagger_client.Body72() # Body72 | The Tgstation.Server.Api.Models.UserGroup to update. (optional)

try:
    # Update a Tgstation.Server.Api.Models.UserGroup.
    api_response = api_instance.user_group_controller_update(api, user_agent, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserGroupApi->user_group_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **body** | [**Body72**](Body72.md)| The Tgstation.Server.Api.Models.UserGroup to update. | [optional] 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


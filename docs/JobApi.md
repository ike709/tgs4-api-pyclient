# swagger_client.JobApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**job_controller_delete**](JobApi.md#job_controller_delete) | **DELETE** /Job/{id} | Cancel a running Tgstation.Server.Api.Models.Response.JobResponse.
[**job_controller_get_id**](JobApi.md#job_controller_get_id) | **GET** /Job/{id} | Get a specific Tgstation.Server.Api.Models.Response.JobResponse.
[**job_controller_list**](JobApi.md#job_controller_list) | **GET** /Job/List | List all Tgstation.Server.Api.Models.Response.JobResponse for the instance in reverse creation order.
[**job_controller_read**](JobApi.md#job_controller_read) | **GET** /Job | Get active Tgstation.Server.Api.Models.Response.JobResponses for the instance.

# **job_controller_delete**
> JobResponse job_controller_delete(api, user_agent, instance, id)

Cancel a running Tgstation.Server.Api.Models.Response.JobResponse.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Response.JobResponse to cancel.

try:
    # Cancel a running Tgstation.Server.Api.Models.Response.JobResponse.
    api_response = api_instance.job_controller_delete(api, user_agent, instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Response.JobResponse to cancel. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_controller_get_id**
> JobResponse job_controller_get_id(api, user_agent, instance, id)

Get a specific Tgstation.Server.Api.Models.Response.JobResponse.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Response.JobResponse to retrieve.

try:
    # Get a specific Tgstation.Server.Api.Models.Response.JobResponse.
    api_response = api_instance.job_controller_get_id(api, user_agent, instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id of the Tgstation.Server.Api.Models.Response.JobResponse to retrieve. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_controller_list**
> PaginatedJobResponse job_controller_list(api, user_agent, instance, page=page, page_size=page_size)

List all Tgstation.Server.Api.Models.Response.JobResponse for the instance in reverse creation order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # List all Tgstation.Server.Api.Models.Response.JobResponse for the instance in reverse creation order.
    api_response = api_instance.job_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_list: %s\n" % e)
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

[**PaginatedJobResponse**](PaginatedJobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_controller_read**
> PaginatedJobResponse job_controller_read(api, user_agent, instance, page=page, page_size=page_size)

Get active Tgstation.Server.Api.Models.Response.JobResponses for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.JobApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Get active Tgstation.Server.Api.Models.Response.JobResponses for the instance.
    api_response = api_instance.job_controller_read(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->job_controller_read: %s\n" % e)
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

[**PaginatedJobResponse**](PaginatedJobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


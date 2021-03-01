# swagger_client.DreamMakerApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dream_maker_controller_create**](DreamMakerApi.md#dream_maker_controller_create) | **PUT** /DreamMaker | Begin deploying repository code.
[**dream_maker_controller_get_id**](DreamMakerApi.md#dream_maker_controller_get_id) | **GET** /DreamMaker/{id} | Get a Tgstation.Server.Host.Models.CompileJob specified by a given id.
[**dream_maker_controller_list**](DreamMakerApi.md#dream_maker_controller_list) | **GET** /DreamMaker/List | List all Tgstation.Server.Host.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.
[**dream_maker_controller_read**](DreamMakerApi.md#dream_maker_controller_read) | **GET** /DreamMaker | Read current deployment settings.
[**dream_maker_controller_update**](DreamMakerApi.md#dream_maker_controller_update) | **POST** /DreamMaker | Update deployment settings.

# **dream_maker_controller_create**
> JobResponse dream_maker_controller_create(api, user_agent, instance)

Begin deploying repository code.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Begin deploying repository code.
    api_response = api_instance.dream_maker_controller_create(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_create: %s\n" % e)
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

# **dream_maker_controller_get_id**
> CompileJobResponse dream_maker_controller_get_id(api, user_agent, instance, id)

Get a Tgstation.Server.Host.Models.CompileJob specified by a given id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id.

try:
    # Get a Tgstation.Server.Host.Models.CompileJob specified by a given id.
    api_response = api_instance.dream_maker_controller_get_id(api, user_agent, instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id. | 

### Return type

[**CompileJobResponse**](CompileJobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_maker_controller_list**
> PaginatedCompileJobResponse dream_maker_controller_list(api, user_agent, instance, page=page, page_size=page_size)

List all Tgstation.Server.Host.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # List all Tgstation.Server.Host.Models.CompileJobTgstation.Server.Api.Models.EntityIds for the instance.
    api_response = api_instance.dream_maker_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_list: %s\n" % e)
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

[**PaginatedCompileJobResponse**](PaginatedCompileJobResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_maker_controller_read**
> DreamMakerResponse dream_maker_controller_read(api, user_agent, instance)

Read current deployment settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Read current deployment settings.
    api_response = api_instance.dream_maker_controller_read(api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**DreamMakerResponse**](DreamMakerResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dream_maker_controller_update**
> DreamMakerResponse dream_maker_controller_update(body, api, user_agent, instance)

Update deployment settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DreamMakerApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body32() # Body32 | The Tgstation.Server.Api.Models.Request.DreamMakerRequest.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Update deployment settings.
    api_response = api_instance.dream_maker_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DreamMakerApi->dream_maker_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)| The Tgstation.Server.Api.Models.Request.DreamMakerRequest. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**DreamMakerResponse**](DreamMakerResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


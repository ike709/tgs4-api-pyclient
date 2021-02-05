# swagger_client.ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_controller_create**](ChatApi.md#chat_controller_create) | **PUT** /Chat | Create a new chat bot model.
[**chat_controller_delete**](ChatApi.md#chat_controller_delete) | **DELETE** /Chat/{id} | Delete a Tgstation.Server.Api.Models.ChatBot.
[**chat_controller_get_id**](ChatApi.md#chat_controller_get_id) | **GET** /Chat/{id} | Get a specific Tgstation.Server.Api.Models.ChatBot.
[**chat_controller_list**](ChatApi.md#chat_controller_list) | **GET** /Chat/List | List Tgstation.Server.Api.Models.ChatBots.
[**chat_controller_update**](ChatApi.md#chat_controller_update) | **POST** /Chat | Updates a chat bot model.

# **chat_controller_create**
> ChatBot chat_controller_create(api, user_agent, instance, body=body)

Create a new chat bot model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
body = swagger_client.Body8() # Body8 | The Tgstation.Server.Api.Models.ChatBot to create. (optional)

try:
    # Create a new chat bot model.
    api_response = api_instance.chat_controller_create(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_controller_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body8**](Body8.md)| The Tgstation.Server.Api.Models.ChatBot to create. | [optional] 

### Return type

[**ChatBot**](ChatBot.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_controller_delete**
> chat_controller_delete(api, user_agent, instance, id)

Delete a Tgstation.Server.Api.Models.ChatBot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id to delete.

try:
    # Delete a Tgstation.Server.Api.Models.ChatBot.
    api_instance.chat_controller_delete(api, user_agent, instance, id)
except ApiException as e:
    print("Exception when calling ChatApi->chat_controller_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id to delete. | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_controller_get_id**
> ChatBot chat_controller_get_id(api, user_agent, instance, id)

Get a specific Tgstation.Server.Api.Models.ChatBot.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
id = 789 # int | The Tgstation.Server.Api.Models.EntityId.Id to retrieve.

try:
    # Get a specific Tgstation.Server.Api.Models.ChatBot.
    api_response = api_instance.chat_controller_get_id(api, user_agent, instance, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_controller_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **id** | **int**| The Tgstation.Server.Api.Models.EntityId.Id to retrieve. | 

### Return type

[**ChatBot**](ChatBot.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_controller_list**
> PaginatedChatBot chat_controller_list(api, user_agent, instance, page=page, page_size=page_size)

List Tgstation.Server.Api.Models.ChatBots.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # List Tgstation.Server.Api.Models.ChatBots.
    api_response = api_instance.chat_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_controller_list: %s\n" % e)
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

[**PaginatedChatBot**](PaginatedChatBot.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chat_controller_update**
> ChatBot chat_controller_update(api, user_agent, instance, body=body)

Updates a chat bot model.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ChatApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
body = swagger_client.Body12() # Body12 | The Tgstation.Server.Api.Models.ChatBot update to apply. (optional)

try:
    # Updates a chat bot model.
    api_response = api_instance.chat_controller_update(api, user_agent, instance, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **body** | [**Body12**](Body12.md)| The Tgstation.Server.Api.Models.ChatBot update to apply. | [optional] 

### Return type

[**ChatBot**](ChatBot.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


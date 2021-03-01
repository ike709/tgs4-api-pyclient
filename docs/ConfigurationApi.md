# swagger_client.ConfigurationApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_controller_create_directory**](ConfigurationApi.md#configuration_controller_create_directory) | **PUT** /Config | Create a configuration directory.
[**configuration_controller_delete_directory**](ConfigurationApi.md#configuration_controller_delete_directory) | **DELETE** /Config | Deletes an empty directory
[**configuration_controller_directory**](ConfigurationApi.md#configuration_controller_directory) | **GET** /Config/List/{directoryPath} | Get the contents of a directory at a directoryPath
[**configuration_controller_file**](ConfigurationApi.md#configuration_controller_file) | **GET** /Config/File/{filePath} | Get the contents of a file at a filePath
[**configuration_controller_list**](ConfigurationApi.md#configuration_controller_list) | **GET** /Config/List | Get the contents of the root configuration directory.
[**configuration_controller_update**](ConfigurationApi.md#configuration_controller_update) | **POST** /Config | Write to a configuration file.

# **configuration_controller_create_directory**
> ConfigurationFileResponse configuration_controller_create_directory(body, api, user_agent, instance)

Create a configuration directory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body16() # Body16 | The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the directory.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Create a configuration directory.
    api_response = api_instance.configuration_controller_create_directory(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_create_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)| The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the directory. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**ConfigurationFileResponse**](ConfigurationFileResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_delete_directory**
> configuration_controller_delete_directory(body, api, user_agent, instance)

Deletes an empty directory

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body24() # Body24 | A Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the path to the directory to delete
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Deletes an empty directory
    api_instance.configuration_controller_delete_directory(body, api, user_agent, instance)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_delete_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body24**](Body24.md)| A Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the path to the directory to delete | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_directory**
> PaginatedConfigurationFileResponse configuration_controller_directory(api, user_agent, instance, directory_path, page=page, page_size=page_size)

Get the contents of a directory at a directoryPath

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
directory_path = 'directory_path_example' # str | The path of the directory to get
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Get the contents of a directory at a directoryPath
    api_response = api_instance.configuration_controller_directory(api, user_agent, instance, directory_path, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **directory_path** | **str**| The path of the directory to get | 
 **page** | **int**| The current page. | [optional] 
 **page_size** | **int**| The page size. | [optional] 

### Return type

[**PaginatedConfigurationFileResponse**](PaginatedConfigurationFileResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_file**
> ConfigurationFileResponse configuration_controller_file(api, user_agent, instance, file_path)

Get the contents of a file at a filePath

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
file_path = 'file_path_example' # str | The path of the file to get

try:
    # Get the contents of a file at a filePath
    api_response = api_instance.configuration_controller_file(api, user_agent, instance, file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 
 **file_path** | **str**| The path of the file to get | 

### Return type

[**ConfigurationFileResponse**](ConfigurationFileResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_list**
> PaginatedConfigurationFileResponse configuration_controller_list(api, user_agent, instance, page=page, page_size=page_size)

Get the contents of the root configuration directory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed
page = 56 # int | The current page. (optional)
page_size = 56 # int | The page size. (optional)

try:
    # Get the contents of the root configuration directory.
    api_response = api_instance.configuration_controller_list(api, user_agent, instance, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_list: %s\n" % e)
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

[**PaginatedConfigurationFileResponse**](PaginatedConfigurationFileResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_controller_update**
> ConfigurationFileResponse configuration_controller_update(body, api, user_agent, instance)

Write to a configuration file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.Body20() # Body20 | The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the file.
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
instance = 56 # int | The instance ID being accessed

try:
    # Write to a configuration file.
    api_response = api_instance.configuration_controller_update(body, api, user_agent, instance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_controller_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body20**](Body20.md)| The Tgstation.Server.Api.Models.Request.ConfigurationFileRequest representing the file. | 
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **instance** | **int**| The instance ID being accessed | 

### Return type

[**ConfigurationFileResponse**](ConfigurationFileResponse.md)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


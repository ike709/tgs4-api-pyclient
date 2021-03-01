# swagger_client.HomeApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**home_controller_create_token**](HomeApi.md#home_controller_create_token) | **POST** / | Attempt to authenticate a Tgstation.Server.Host.Models.User using Tgstation.Server.Host.Controllers.ApiController.ApiHeaders
[**home_controller_home**](HomeApi.md#home_controller_home) | **GET** / | Main page of the Tgstation.Server.Host.Core.Application

# **home_controller_create_token**
> TokenResponse home_controller_create_token(api, user_agent, o_auth_provider=o_auth_provider)

Attempt to authenticate a Tgstation.Server.Host.Models.User using Tgstation.Server.Host.Controllers.ApiController.ApiHeaders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: OAuth_Login_Scheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'# Configure HTTP basic authorization: Password_Login_Scheme
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.HomeApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
o_auth_provider = 'o_auth_provider_example' # str | The external OAuth service provider. (optional)

try:
    # Attempt to authenticate a Tgstation.Server.Host.Models.User using Tgstation.Server.Host.Controllers.ApiController.ApiHeaders
    api_response = api_instance.home_controller_create_token(api, user_agent, o_auth_provider=o_auth_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->home_controller_create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **o_auth_provider** | **str**| The external OAuth service provider. | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[OAuth_Login_Scheme](../README.md#OAuth_Login_Scheme), [Password_Login_Scheme](../README.md#Password_Login_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **home_controller_home**
> ServerInformationResponse home_controller_home(api, user_agent)

Main page of the Tgstation.Server.Host.Core.Application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.

try:
    # Main page of the Tgstation.Server.Host.Core.Application
    api_response = api_instance.home_controller_home(api, user_agent)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->home_controller_home: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 

### Return type

[**ServerInformationResponse**](ServerInformationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


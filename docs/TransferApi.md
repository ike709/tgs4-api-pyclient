# swagger_client.TransferApi

All URIs are relative to *http://localhost:5010*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfer_controller_download**](TransferApi.md#transfer_controller_download) | **GET** /Transfer | Downloads a file with a given ticket.
[**transfer_controller_upload**](TransferApi.md#transfer_controller_upload) | **PUT** /Transfer | Uploads a file with a given ticket.

# **transfer_controller_download**
> str transfer_controller_download(api, user_agent, ticket)

Downloads a file with a given ticket.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TransferApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
ticket = 'ticket_example' # str | The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the download.

try:
    # Downloads a file with a given ticket.
    api_response = api_instance.transfer_controller_download(api, user_agent, ticket)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransferApi->transfer_controller_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **ticket** | **str**| The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the download. | 

### Return type

**str**

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_controller_upload**
> transfer_controller_upload(api, user_agent, ticket, body=body)

Uploads a file with a given ticket.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.TransferApi(swagger_client.ApiClient(configuration))
api = 'api_example' # str | The API version being used in the form \"Tgstation.Server.Api/[API version]\"
user_agent = 'user_agent_example' # str | The user agent of the calling client.
ticket = 'ticket_example' # str | The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the upload.
body = swagger_client.Object() # Object |  (optional)

try:
    # Uploads a file with a given ticket.
    api_instance.transfer_controller_upload(api, user_agent, ticket, body=body)
except ApiException as e:
    print("Exception when calling TransferApi->transfer_controller_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api** | **str**| The API version being used in the form \&quot;Tgstation.Server.Api/[API version]\&quot; | 
 **user_agent** | **str**| The user agent of the calling client. | 
 **ticket** | **str**| The Tgstation.Server.Api.Models.Response.FileTicketResponse.FileTicket for the upload. | 
 **body** | **Object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Token_Authorization_Scheme](../README.md#Token_Authorization_Scheme)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


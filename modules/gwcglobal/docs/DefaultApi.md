# gs_rest_api_gwcglobal.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_get**](DefaultApi.md#global_get) | **GET** /global | Retrieve the global server configuration
[**global_put**](DefaultApi.md#global_put) | **PUT** /global | Modifies the global configuration.

# **global_get**
> ModelGlobal global_get()

Retrieve the global server configuration

Retrieves configuration details about the GeoWebCache server as a whole.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcglobal
from gs_rest_api_gwcglobal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcglobal.DefaultApi()

try:
    # Retrieve the global server configuration
    api_response = api_instance.global_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->global_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelGlobal**](ModelGlobal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_put**
> global_put(body)

Modifies the global configuration.

Update one or more global configuration values

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcglobal
from gs_rest_api_gwcglobal.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcglobal.DefaultApi()
body = gs_rest_api_gwcglobal.ModelGlobal() # ModelGlobal | The modified global configuration.

try:
    # Modifies the global configuration.
    api_instance.global_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->global_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelGlobal**](ModelGlobal.md)| The modified global configuration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


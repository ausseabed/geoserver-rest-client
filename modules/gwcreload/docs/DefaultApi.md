# gs_rest_api_gwcreload.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reload_post**](DefaultApi.md#reload_post) | **POST** /reload | Reloads GWC settings/

# **reload_post**
> reload_post(body=body)

Reloads GWC settings/

Reloads the GeoWebCache settings after making changes to the configuration.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcreload
from gs_rest_api_gwcreload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcreload.DefaultApi()
body = 'body_example' # str | The string value of the configuration ie. "reload_configuration=1" (optional)

try:
    # Reloads GWC settings/
    api_instance.reload_post(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The string value of the configuration ie. &quot;reload_configuration&#x3D;1&quot; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


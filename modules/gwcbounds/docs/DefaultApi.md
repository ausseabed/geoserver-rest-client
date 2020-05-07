# gs_rest_api_gwcbounds.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bounds_get**](DefaultApi.md#bounds_get) | **GET** /bounds/{layer}/{srs}/{type} | Returns the bounds for a layer based on srs.

# **bounds_get**
> bounds_get(layer, srs, type)

Returns the bounds for a layer based on srs.

Returns the bounds for a layer based on srs.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcbounds
from gs_rest_api_gwcbounds.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcbounds.DefaultApi()
layer = 'layer_example' # str | The name of the layer to update.
srs = 'srs_example' # str | The srs projection used against the layer to find the bounds such as EPSG:4326
type = 'type_example' # str | Accepts java as an extension.

try:
    # Returns the bounds for a layer based on srs.
    api_instance.bounds_get(layer, srs, type)
except ApiException as e:
    print("Exception when calling DefaultApi->bounds_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| The name of the layer to update. | 
 **srs** | **str**| The srs projection used against the layer to find the bounds such as EPSG:4326 | 
 **type** | **str**| Accepts java as an extension. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


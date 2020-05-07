# gs_rest_api_gwcdiskquota.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disk_quota_get**](DefaultApi.md#disk_quota_get) | **GET** /diskquota | Returns the gwc Quota configuration
[**disk_quota_put**](DefaultApi.md#disk_quota_put) | **PUT** /diskquota | Modify properties of a gwc instance disk quota configuration.

# **disk_quota_get**
> disk_quota_get()

Returns the gwc Quota configuration

Returns the GeoWebCache DiskQuota configurations which include disk usage limits and expritation policies for a gwc instance.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcdiskquota
from gs_rest_api_gwcdiskquota.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcdiskquota.DefaultApi()

try:
    # Returns the gwc Quota configuration
    api_instance.disk_quota_get()
except ApiException as e:
    print("Exception when calling DefaultApi->disk_quota_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, appliction/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disk_quota_put**
> disk_quota_put(body=body)

Modify properties of a gwc instance disk quota configuration.

The request body for PUT should contain desired properties to be modified.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcdiskquota
from gs_rest_api_gwcdiskquota.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcdiskquota.DefaultApi()
body = gs_rest_api_gwcdiskquota.DiskQuota() # DiskQuota | The diskquota configuration with modified property values. (optional)

try:
    # Modify properties of a gwc instance disk quota configuration.
    api_instance.disk_quota_put(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->disk_quota_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DiskQuota**](DiskQuota.md)| The diskquota configuration with modified property values. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# gs_rest_api_gwcseed.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layer_seed_get**](DefaultApi.md#layer_seed_get) | **GET** /seed/{layer}.{format} | Query&#x27;s the currently running GWC task for a given layer
[**layer_seed_post**](DefaultApi.md#layer_seed_post) | **POST** /seed/{layer}.{format} | Issue a seed, reseed or truncate task request
[**seed_get**](DefaultApi.md#seed_get) | **GET** /seed.json | Query&#x27;s currently running GWC task

# **layer_seed_get**
> layer_seed_get(layer, format)

Query's the currently running GWC task for a given layer

Returns HTML of the GeoWebCache Seed ui page or a json array of the status for currently running task of a given layer if using json extension. The json array contains a set of long in the following order:[tiles processed, total number of tiles to process, number of remaining tiles, Task ID, Task status]

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcseed
from gs_rest_api_gwcseed.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcseed.DefaultApi()
layer = 'layer_example' # str | The name of the layer to query GWC task.
format = 'format_example' # str | Based on format, the request will return an application/html or application/json response.

try:
    # Query's the currently running GWC task for a given layer
    api_instance.layer_seed_get(layer, format)
except ApiException as e:
    print("Exception when calling DefaultApi->layer_seed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| The name of the layer to query GWC task. | 
 **format** | **str**| Based on format, the request will return an application/html or application/json response. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layer_seed_post**
> layer_seed_post(layer, body=body)

Issue a seed, reseed or truncate task request

Executes an issue to seed, reseed or truncate task request for a layer and returns HTML UI page of running GWC tasks and tasks to execute.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcseed
from gs_rest_api_gwcseed.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcseed.DefaultApi()
layer = 'layer_example' # str | The name of the layer to query GWC task.
body = gs_rest_api_gwcseed.SeedRequest() # SeedRequest | The updated layer definition. (optional)

try:
    # Issue a seed, reseed or truncate task request
    api_instance.layer_seed_post(layer, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->layer_seed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer** | **str**| The name of the layer to query GWC task. | 
 **body** | [**SeedRequest**](SeedRequest.md)| The updated layer definition. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seed_get**
> seed_get()

Query's currently running GWC task

Query's and returns a json array of the status for all currently running task. Requires json extension in the request. The array contains a set of long in the following order:[tiles processed, total number of tiles to process, number of remaining tiles, Task ID, Task status]. The returned task status will be one of -1 = ABORTED, 0 = PENDING, 1 = RUNNING, 2 = DONE

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcseed
from gs_rest_api_gwcseed.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcseed.DefaultApi()

try:
    # Query's currently running GWC task
    api_instance.seed_get()
except ApiException as e:
    print("Exception when calling DefaultApi->seed_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


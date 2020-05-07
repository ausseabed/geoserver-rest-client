# gs_rest_api_gwclayers.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**layers_get**](DefaultApi.md#layers_get) | **GET** /layers | Get a list of cached layers
[**layers_name_delete**](DefaultApi.md#layers_name_delete) | **DELETE** /layers/{layerName} | Delete cached layer
[**layers_name_get**](DefaultApi.md#layers_name_get) | **GET** /layers/{layerName} | Retrieve a cached layer
[**layers_name_post**](DefaultApi.md#layers_name_post) | **POST** /layers/{layerName} | Modify a cached layer (Deprecated).
[**layers_name_put**](DefaultApi.md#layers_name_put) | **PUT** /layers/{layerName} | Create or update a cached layer.

# **layers_get**
> Layers layers_get()

Get a list of cached layers

Displays a list of all cached layers on the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwclayers
from gs_rest_api_gwclayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwclayers.DefaultApi()

try:
    # Get a list of cached layers
    api_response = api_instance.layers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Layers**](Layers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_delete**
> layers_name_delete(layer_name)

Delete cached layer

Deletes a cached layer from the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwclayers
from gs_rest_api_gwclayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwclayers.DefaultApi()
layer_name = 'layer_name_example' # str | The name of the layer to delete.

try:
    # Delete cached layer
    api_instance.layers_name_delete(layer_name)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**| The name of the layer to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_get**
> Layer layers_name_get(layer_name)

Retrieve a cached layer

Retrieves a single cached layer definition.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwclayers
from gs_rest_api_gwclayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwclayers.DefaultApi()
layer_name = 'layer_name_example' # str | The name of the layer to retrieve.

try:
    # Retrieve a cached layer
    api_response = api_instance.layers_name_get(layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer_name** | **str**| The name of the layer to retrieve. | 

### Return type

[**Layer**](Layer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_post**
> layers_name_post(body, layer_name)

Modify a cached layer (Deprecated).

Modifies an existing cached layer on the server. Deprecated - use PUT instead.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwclayers
from gs_rest_api_gwclayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwclayers.DefaultApi()
body = gs_rest_api_gwclayers.Layer() # Layer | The updated layer definition.
layer_name = 'layer_name_example' # str | The name of the layer to modify.

try:
    # Modify a cached layer (Deprecated).
    api_instance.layers_name_post(body, layer_name)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer**](Layer.md)| The updated layer definition. | 
 **layer_name** | **str**| The name of the layer to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **layers_name_put**
> layers_name_put(body, layer_name)

Create or update a cached layer.

Creates a new cached layer on the server, or modifies an existing cached layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwclayers
from gs_rest_api_gwclayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwclayers.DefaultApi()
body = gs_rest_api_gwclayers.Layer() # Layer | The new layer definition.
layer_name = 'layer_name_example' # str | The name of the layer to add.

try:
    # Create or update a cached layer.
    api_instance.layers_name_put(body, layer_name)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer**](Layer.md)| The new layer definition. | 
 **layer_name** | **str**| The name of the layer to add. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# gs_rest_api_reload.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_reload**](DefaultApi.md#delete_reload) | **DELETE** /reload | 
[**delete_reset**](DefaultApi.md#delete_reset) | **DELETE** /reset | 
[**get_reload**](DefaultApi.md#get_reload) | **GET** /reload | 
[**get_reset**](DefaultApi.md#get_reset) | **GET** /reset | 
[**post_reload**](DefaultApi.md#post_reload) | **POST** /reload | Reload the configuration from disk, and reset all caches.
[**post_reset**](DefaultApi.md#post_reset) | **POST** /reset | Reset all store, raster, and schema caches.
[**put_reload**](DefaultApi.md#put_reload) | **PUT** /reload | Reload the configuration from disk, and reset all caches.
[**put_reset**](DefaultApi.md#put_reset) | **PUT** /reset | Reset all store, raster, and schema caches.

# **delete_reload**
> delete_reload()



Invalid. Use PUT or POST to reload the catalog and configuation.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    api_instance.delete_reload()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_reload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reset**
> delete_reset()



Invalid. Use PUT or POST to reset the caches.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    api_instance.delete_reset()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reload**
> get_reload()



Invalid. Use PUT or POST to reload the catalog and configuation.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    api_instance.get_reload()
except ApiException as e:
    print("Exception when calling DefaultApi->get_reload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reset**
> get_reset()



Invalid. Use PUT or POST to reset the caches.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    api_instance.get_reset()
except ApiException as e:
    print("Exception when calling DefaultApi->get_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reload**
> post_reload()

Reload the configuration from disk, and reset all caches.

Reloads the GeoServer catalog and configuration from disk. This operation is used in cases where an external tool has modified the on-disk configuration. This operation will also force GeoServer to drop any internal caches and reconnect to all data stores.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    # Reload the configuration from disk, and reset all caches.
    api_instance.post_reload()
except ApiException as e:
    print("Exception when calling DefaultApi->post_reload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_reset**
> post_reset()

Reset all store, raster, and schema caches.

Resets all store, raster, and schema caches. This operation is used to force GeoServer to drop all caches and store connections and reconnect to each of them the next time they are needed by a request. This is useful in case the stores themselves cache some information about the data structures they manage that may have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    # Reset all store, raster, and schema caches.
    api_instance.post_reset()
except ApiException as e:
    print("Exception when calling DefaultApi->post_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reload**
> put_reload()

Reload the configuration from disk, and reset all caches.

Reloads the GeoServer catalog and configuration from disk. This operation is used in cases where an external tool has modified the on-disk configuration. This operation will also force GeoServer to drop any internal caches and reconnect to all data stores.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    # Reload the configuration from disk, and reset all caches.
    api_instance.put_reload()
except ApiException as e:
    print("Exception when calling DefaultApi->put_reload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_reset**
> put_reset()

Reset all store, raster, and schema caches.

Resets all store, raster, and schema caches. This operation is used to force GeoServer to drop all caches and store connections and reconnect to each of them the next time they are needed by a request. This is useful in case the stores themselves cache some information about the data structures they manage that may have changed in the meantime.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_reload
from gs_rest_api_reload.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_reload.DefaultApi()

try:
    # Reset all store, raster, and schema caches.
    api_instance.put_reset()
except ApiException as e:
    print("Exception when calling DefaultApi->put_reset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


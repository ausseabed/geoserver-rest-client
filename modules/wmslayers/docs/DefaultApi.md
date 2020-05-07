# gs_rest_api_wmslayers.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wms_store_layer**](DefaultApi.md#delete_wms_store_layer) | **DELETE** /workspaces/{workspace}/wmslayers/{wmslayer} | 
[**delete_wms_store_layers**](DefaultApi.md#delete_wms_store_layers) | **DELETE** /workspaces/{workspace}/wmslayers | 
[**delete_wms_store_store_layer**](DefaultApi.md#delete_wms_store_store_layer) | **DELETE** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers/{wmslayer} | 
[**delete_wms_store_store_layers**](DefaultApi.md#delete_wms_store_store_layers) | **DELETE** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers | 
[**get_wms_store_layer**](DefaultApi.md#get_wms_store_layer) | **GET** /workspaces/{workspace}/wmslayers/{wmslayer} | 
[**get_wms_store_layers**](DefaultApi.md#get_wms_store_layers) | **GET** /workspaces/{workspace}/wmslayers | 
[**get_wms_store_store_layer**](DefaultApi.md#get_wms_store_store_layer) | **GET** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers/{wmslayer} | 
[**get_wms_store_store_layers**](DefaultApi.md#get_wms_store_store_layers) | **GET** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers | 
[**post_wms_store_layer**](DefaultApi.md#post_wms_store_layer) | **POST** /workspaces/{workspace}/wmslayers/{wmslayer} | 
[**post_wms_store_layers**](DefaultApi.md#post_wms_store_layers) | **POST** /workspaces/{workspace}/wmslayers | 
[**post_wms_store_store_layer**](DefaultApi.md#post_wms_store_store_layer) | **POST** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers/{wmslayer} | 
[**post_wms_store_store_layers**](DefaultApi.md#post_wms_store_store_layers) | **POST** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers | 
[**put_wms_store_layer**](DefaultApi.md#put_wms_store_layer) | **PUT** /workspaces/{workspace}/wmslayers/{wmslayer} | 
[**put_wms_store_layers**](DefaultApi.md#put_wms_store_layers) | **PUT** /workspaces/{workspace}/wmslayers | 
[**put_wms_store_store_layer**](DefaultApi.md#put_wms_store_store_layer) | **PUT** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers/{wmslayer} | 
[**put_wms_store_store_layers**](DefaultApi.md#put_wms_store_store_layers) | **PUT** /workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers | 

# **delete_wms_store_layer**
> delete_wms_store_layer(workspace, wmslayer, recurse=recurse)



Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
wmslayer = 'wmslayer_example' # str | Name of the layer to be deleted
recurse = true # bool | Recursively deletes all layers referenced by the specified wmslayer. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the wmslayer. (optional)

try:
    api_instance.delete_wms_store_layer(workspace, wmslayer, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmslayer** | **str**| Name of the layer to be deleted | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified wmslayer. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layers reference the wmslayer. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wms_store_layers**
> delete_wms_store_layers()



Invalid. Can only delete an individual layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.delete_wms_store_layers()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_store_layers: %s\n" % e)
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

# **delete_wms_store_store_layer**
> delete_wms_store_store_layer(workspace, wmsstore, wmslayer, recurse=recurse)



Deletes a layer from the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
wmsstore = 'wmsstore_example' # str | Name of the store
wmslayer = 'wmslayer_example' # str | Name of the layer to be deleted
recurse = true # bool | Recursively deletes all layers referenced by the specified wmslayer. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layers reference the wmslayer. (optional)

try:
    api_instance.delete_wms_store_store_layer(workspace, wmsstore, wmslayer, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmsstore** | **str**| Name of the store | 
 **wmslayer** | **str**| Name of the layer to be deleted | 
 **recurse** | **bool**| Recursively deletes all layers referenced by the specified wmslayer. Allowed values for this parameter are true or false. The default value is false. A request with &#x27;recurse&#x3D;false&#x27; will fail if any layers reference the wmslayer. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wms_store_store_layers**
> delete_wms_store_store_layers()



Invalid. Can only delete an individual layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.delete_wms_store_store_layers()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_store_store_layers: %s\n" % e)
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

# **get_wms_store_layer**
> WMSStoreLayerInfo get_wms_store_layer(workspace, wmslayer, quiet_on_not_found=quiet_on_not_found)



Retrieves an individual WMS layer. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmslayers/{wmslayer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
wmslayer = 'wmslayer_example' # str | Name of the layer
quiet_on_not_found = true # bool | When set to \"true\", will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \"true\" or \"false\" (default). (optional)

try:
    api_response = api_instance.get_wms_store_layer(workspace, wmslayer, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmslayer** | **str**| Name of the layer | 
 **quiet_on_not_found** | **bool**| When set to \&quot;true\&quot;, will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). | [optional] 

### Return type

[**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_store_layers**
> WMSStoreLayersList get_wms_store_layers(workspace, list=list)



Retrieves the WMS layers available on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmslayers\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
list = 'list_example' # str | Set \"list=available\" to see all possible layers in the store, not just ones currently published (optional)

try:
    api_response = api_instance.get_wms_store_layers(workspace, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **list** | **str**| Set \&quot;list&#x3D;available\&quot; to see all possible layers in the store, not just ones currently published | [optional] 

### Return type

[**WMSStoreLayersList**](WMSStoreLayersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html, application/xml (list=available), application/json (list=available)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_store_store_layer**
> WMSStoreLayerInfo get_wms_store_store_layer(workspace, wmsstore, wmslayer, quiet_on_not_found=quiet_on_not_found)



Retrieves an individual WMS store layer for a given store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers/{wmslayer}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
wmsstore = 'wmsstore_example' # str | Name of the store
wmslayer = 'wmslayer_example' # str | Name of the layer
quiet_on_not_found = true # bool | When set to \"true\", will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \"true\" or \"false\" (default). (optional)

try:
    api_response = api_instance.get_wms_store_store_layer(workspace, wmsstore, wmslayer, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmsstore** | **str**| Name of the store | 
 **wmslayer** | **str**| Name of the layer | 
 **quiet_on_not_found** | **bool**| When set to \&quot;true\&quot;, will not log an exception when the style is not present. The 404 status code will still be returned. Allowable values are \&quot;true\&quot; or \&quot;false\&quot; (default). | [optional] 

### Return type

[**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_store_store_layers**
> WMSStoreLayersList get_wms_store_store_layers(workspace, wmsstore, list=list)



Retrieves the WMS store layers available in the given store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmsstores/{wmsstore}/wmslayers.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace
wmsstore = 'wmsstore_example' # str | Name of the store
list = 'list_example' # str | Set \"list=available\" to see all possible layers in the store, not just ones currently published (optional)

try:
    api_response = api_instance.get_wms_store_store_layers(workspace, wmsstore, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_store_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace | 
 **wmsstore** | **str**| Name of the store | 
 **list** | **str**| Set \&quot;list&#x3D;available\&quot; to see all possible layers in the store, not just ones currently published | [optional] 

### Return type

[**WMSStoreLayersList**](WMSStoreLayersList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html, application/xml (list=available), application/json (list=available)

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wms_store_layer**
> post_wms_store_layer()



Invalid. Use PUT to edit a layer, or POST on the /wmslayers endpoint to add a new layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.post_wms_store_layer()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_store_layer: %s\n" % e)
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

# **post_wms_store_layers**
> post_wms_store_layers(body, workspace)



Publishes a new WMS store layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
body = gs_rest_api_wmslayers.WMSStoreLayerInfo() # WMSStoreLayerInfo | Body of the WMS store layer
workspace = 'workspace_example' # str | Name of the workspace

try:
    api_instance.post_wms_store_layers(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)| Body of the WMS store layer | 
 **workspace** | **str**| Name of the workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wms_store_store_layer**
> post_wms_store_store_layer()



Invalid. Use PUT to edit a layer, or POST on the /wmslayers endpoint to add a new layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.post_wms_store_store_layer()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_store_store_layer: %s\n" % e)
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

# **post_wms_store_store_layers**
> post_wms_store_store_layers(body, workspace, wmsstore)



Publishes a new WMS store layer in the given store.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
body = gs_rest_api_wmslayers.WMSStoreLayerInfo() # WMSStoreLayerInfo | Body of the WMS store layer
workspace = 'workspace_example' # str | Name of the workspace
wmsstore = 'wmsstore_example' # str | Name of the data store

try:
    api_instance.post_wms_store_store_layers(body, workspace, wmsstore)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_store_store_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)| Body of the WMS store layer | 
 **workspace** | **str**| Name of the workspace | 
 **wmsstore** | **str**| Name of the data store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_store_layer**
> put_wms_store_layer(body, workspace, wmslayer, calculate=calculate)



Edits an existing WMS store layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
body = gs_rest_api_wmslayers.WMSStoreLayerInfo() # WMSStoreLayerInfo | Body of the WMS store layer
workspace = 'workspace_example' # str | Name of the workspace
wmslayer = 'wmslayer_example' # str | Name of the layer to be edited
calculate = ['calculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a wms layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.put_wms_store_layer(body, workspace, wmslayer, calculate=calculate)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)| Body of the WMS store layer | 
 **workspace** | **str**| Name of the workspace | 
 **wmslayer** | **str**| Name of the layer to be edited | 
 **calculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a wms layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#x27;recalculate&#x3D;&#x27; is useful avoid slow recalculation when operating against large datasets as &#x27;recalculate&#x3D;&#x27; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#x27;recalculate&#x3D;nativebbox&#x27; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#x27;recalculate&#x3D;nativebbox,latlonbbox&#x27; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_store_layers**
> put_wms_store_layers()



Invalid. Use POST for adding a new layer, or PUT on an individual layer to edit it.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.put_wms_store_layers()
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_store_layers: %s\n" % e)
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

# **put_wms_store_store_layer**
> put_wms_store_store_layer(body, workspace, wmsstore, wmslayer, calculate=calculate)



Edits an existing WMS store layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()
body = gs_rest_api_wmslayers.WMSStoreLayerInfo() # WMSStoreLayerInfo | Body of the WMS store layer
workspace = 'workspace_example' # str | Name of the workspace
wmsstore = 'wmsstore_example' # str | Name of the store
wmslayer = 'wmslayer_example' # str | Name of the layer to be edited
calculate = ['calculate_example'] # list[str] | Specifies whether to recalculate any bounding boxes for a wms layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter 'recalculate=' is useful avoid slow recalculation when operating against large datasets as 'recalculate=' avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter 'recalculate=nativebbox' is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - 'recalculate=nativebbox,latlonbbox' can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. (optional)

try:
    api_instance.put_wms_store_store_layer(body, workspace, wmsstore, wmslayer, calculate=calculate)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_store_store_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSStoreLayerInfo**](WMSStoreLayerInfo.md)| Body of the WMS store layer | 
 **workspace** | **str**| Name of the workspace | 
 **wmsstore** | **str**| Name of the store | 
 **wmslayer** | **str**| Name of the layer to be edited | 
 **calculate** | [**list[str]**](str.md)| Specifies whether to recalculate any bounding boxes for a wms layer. Some properties are automatically recalculated when necessary. In particular, the native bounding box is recalculated when the projection or projection policy are changed, and the lat/lon bounding box is recalculated when the native bounding box is recalculated, or when a new native bounding box is explicitly provided in the request. (The native and lat/lon bounding boxes are not automatically recalculated when they are explicitly included in the request.) In addition, the client may explicitly request a fixed set of fields to calculate, by including a comma-separated list of their names in the recalculate parameter.  The empty parameter &#x27;recalculate&#x3D;&#x27; is useful avoid slow recalculation when operating against large datasets as &#x27;recalculate&#x3D;&#x27; avoids calculating any fields, regardless of any changes to projection, projection policy, etc. The nativebbox parameter &#x27;recalculate&#x3D;nativebbox&#x27; is used recalculates the native bounding box, while avoiding recalculating the lat/lon bounding box. Recalculate parameters can be used in together - &#x27;recalculate&#x3D;nativebbox,latlonbbox&#x27; can be used after a bulk import to  to recalculates both the native bounding box and the lat/lon bounding box. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_store_store_layers**
> put_wms_store_store_layers()



Invalid. Use POST for adding a new layer, or PUT on an individual layer to edit it.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmslayers
from gs_rest_api_wmslayers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmslayers.DefaultApi()

try:
    api_instance.put_wms_store_store_layers()
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_store_store_layers: %s\n" % e)
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


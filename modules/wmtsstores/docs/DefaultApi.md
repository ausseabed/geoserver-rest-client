# gs_rest_api_wmtsstores.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wmts_store**](DefaultApi.md#delete_wmts_store) | **DELETE** /workspaces/{workspace}/wmtsstores/{store} | Delete WMTS store
[**delete_wmts_stores**](DefaultApi.md#delete_wmts_stores) | **DELETE** /workspaces/{workspace}/wmtsstores | 
[**get_wmts_store**](DefaultApi.md#get_wmts_store) | **GET** /workspaces/{workspace}/wmtsstores/{store} | Retrieve a WMTS store in a given workspace
[**get_wmts_stores**](DefaultApi.md#get_wmts_stores) | **GET** /workspaces/{workspace}/wmtsstores | Get a list of WMTS stores
[**post_wmts_store**](DefaultApi.md#post_wmts_store) | **POST** /workspaces/{workspace}/wmtsstores/{store} | 
[**post_wmts_stores**](DefaultApi.md#post_wmts_stores) | **POST** /workspaces/{workspace}/wmtsstores | Add a new WMTS store
[**put_wmts_store**](DefaultApi.md#put_wmts_store) | **PUT** /workspaces/{workspace}/wmtsstores/{store} | Modify a single WMTS store.
[**put_wmts_stores**](DefaultApi.md#put_wmts_stores) | **PUT** /workspaces/{workspace}/wmtsstores | 

# **delete_wmts_store**
> delete_wmts_store(workspace, store, recurse=recurse)

Delete WMTS store

Deletes a WMTS store

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()
workspace = 'workspace_example' # str | Name of the workspace containing the WMTS store.
store = 'store_example' # str | Name of the WMTS store
recurse = true # bool | When set to true all resources contained in the store are also removed. (optional)

try:
    # Delete WMTS store
    api_instance.delete_wmts_store(workspace, store, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wmts_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| Name of the workspace containing the WMTS store. | 
 **store** | **str**| Name of the WMTS store | 
 **recurse** | **bool**| When set to true all resources contained in the store are also removed. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wmts_stores**
> delete_wmts_stores()



Invalid. Use /workspaces/{workspace}/wmtsstores/{wmtsstore} instead.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()

try:
    api_instance.delete_wmts_stores()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wmts_stores: %s\n" % e)
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

# **get_wmts_store**
> WMTSStoreInfo get_wmts_store(workspace, store, quiet_on_not_found=quiet_on_not_found)

Retrieve a WMTS store in a given workspace

Displays a representation of the WMTS store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/wmtsstores/{store}.xml\" for XML). Defaults to HTML representation.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace containing the WMTS store.
store = 'store_example' # str | The name of the store to be retrieved
quiet_on_not_found = true # bool | When set to true, avoids to log an Exception when the WMTS store is not present. Note that 404 status code will be returned anyway. (optional)

try:
    # Retrieve a WMTS store in a given workspace
    api_response = api_instance.get_wmts_store(workspace, store, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wmts_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace containing the WMTS store. | 
 **store** | **str**| The name of the store to be retrieved | 
 **quiet_on_not_found** | **bool**| When set to true, avoids to log an Exception when the WMTS store is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

[**WMTSStoreInfo**](WMTSStoreInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_stores**
> WMTSStoresList get_wmts_stores()

Get a list of WMTS stores

Displays a list of all WMTS stores on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/rest/workspaces/{workspace}/wmtsstores.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()

try:
    # Get a list of WMTS stores
    api_response = api_instance.get_wmts_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wmts_stores: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMTSStoresList**](WMTSStoresList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wmts_store**
> post_wmts_store()



Invalid. Use POST on /workspaces/{workspace}/WMTSstores for adding a new WMTS store, or PUT on /workspaces/{workspace}/wmtsstores/{store} to edit/upload an existing WMTS store.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()

try:
    api_instance.post_wmts_store()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wmts_store: %s\n" % e)
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

# **post_wmts_stores**
> post_wmts_stores(body, workspace)

Add a new WMTS store

Adds a new WMTS store entry to the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()
body = gs_rest_api_wmtsstores.WMTSStoreInfo() # WMTSStoreInfo | WMTS store body information to upload.

Examples:
- application/xml:

  ```
  <wmtsStore>
    <name>remote</name>
    <capabilitiesUrl>http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities</capabilitiesUrl>
  </wmtsStore>
  ```

- application/json:

  ```
  {
    "wmtsStore": {
      "name": "remote",
      "capabilitiesUrl": "http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities"
    }
  }
  ```

workspace = 'workspace_example' # str | Name of the worskpace containing the WMTS store.

try:
    # Add a new WMTS store
    api_instance.post_wmts_stores(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wmts_stores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSStoreInfo**](WMTSStoreInfo.md)| WMTS store body information to upload.

Examples:
- application/xml:

  &#x60;&#x60;&#x60;
  &lt;wmtsStore&gt;
    &lt;name&gt;remote&lt;/name&gt;
    &lt;capabilitiesUrl&gt;http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE&#x3D;WMTS&amp;VERSION&#x3D;1.0.0&amp;REQUEST&#x3D;GetCapabilities&lt;/capabilitiesUrl&gt;
  &lt;/wmtsStore&gt;
  &#x60;&#x60;&#x60;

- application/json:

  &#x60;&#x60;&#x60;
  {
    &quot;wmtsStore&quot;: {
      &quot;name&quot;: &quot;remote&quot;,
      &quot;capabilitiesUrl&quot;: &quot;http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE&#x3D;WMTS&amp;VERSION&#x3D;1.0.0&amp;REQUEST&#x3D;GetCapabilities&quot;
    }
  }
  &#x60;&#x60;&#x60;
 | 
 **workspace** | **str**| Name of the worskpace containing the WMTS store. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_store**
> put_wmts_store(body, workspace, store)

Modify a single WMTS store.

Modifies a single WMTS store. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"{store}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()
body = gs_rest_api_wmtsstores.WMTSStoreInfo() # WMTSStoreInfo | WMTS store body information to upload.
For a PUT, only values which should be changed need to be included.

Examples:
- application/xml:

  ```
  <wmtsStore>
    <description>A wmts store</description>
    <enabled>true</enabled>
    <__default>true</__default>
    <capabilitiesUrl>http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities</capabilitiesUrl>
    <user>admin</user>
    <password>geoserver</password>
    <maxConnections>6</maxConnections>
    <readTimeout>60</readTimeout>
    <connectTimeout>30</connectTimeout>
  </wmtsStore>
  ```

- application/json:

  ```
  {
    "wmtsStore": {
      "description": "A wmts store",
      "enabled": "true",
      "_default": "true",
      "capabilitiesUrl": "http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities",
      "user": "admin",
      "password": "geoserver",
      "maxConnections": "6",
      "readTimeout": "60",
      "connectTimeout": "30"
    }
  }
  ```

workspace = 'workspace_example' # str | The name of the workspace containing the WMTS stores.
store = 'store_example' # str | The name of the store to be retrieved

try:
    # Modify a single WMTS store.
    api_instance.put_wmts_store(body, workspace, store)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wmts_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSStoreInfo**](WMTSStoreInfo.md)| WMTS store body information to upload.
For a PUT, only values which should be changed need to be included.

Examples:
- application/xml:

  &#x60;&#x60;&#x60;
  &lt;wmtsStore&gt;
    &lt;description&gt;A wmts store&lt;/description&gt;
    &lt;enabled&gt;true&lt;/enabled&gt;
    &lt;__default&gt;true&lt;/__default&gt;
    &lt;capabilitiesUrl&gt;http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE&#x3D;WMTS&amp;VERSION&#x3D;1.0.0&amp;REQUEST&#x3D;GetCapabilities&lt;/capabilitiesUrl&gt;
    &lt;user&gt;admin&lt;/user&gt;
    &lt;password&gt;geoserver&lt;/password&gt;
    &lt;maxConnections&gt;6&lt;/maxConnections&gt;
    &lt;readTimeout&gt;60&lt;/readTimeout&gt;
    &lt;connectTimeout&gt;30&lt;/connectTimeout&gt;
  &lt;/wmtsStore&gt;
  &#x60;&#x60;&#x60;

- application/json:

  &#x60;&#x60;&#x60;
  {
    &quot;wmtsStore&quot;: {
      &quot;description&quot;: &quot;A wmts store&quot;,
      &quot;enabled&quot;: &quot;true&quot;,
      &quot;_default&quot;: &quot;true&quot;,
      &quot;capabilitiesUrl&quot;: &quot;http://demo.geoserver.org/geoserver/gwc/service/wmts?SERVICE&#x3D;WMTS&amp;VERSION&#x3D;1.0.0&amp;REQUEST&#x3D;GetCapabilities&quot;,
      &quot;user&quot;: &quot;admin&quot;,
      &quot;password&quot;: &quot;geoserver&quot;,
      &quot;maxConnections&quot;: &quot;6&quot;,
      &quot;readTimeout&quot;: &quot;60&quot;,
      &quot;connectTimeout&quot;: &quot;30&quot;
    }
  }
  &#x60;&#x60;&#x60;
 | 
 **workspace** | **str**| The name of the workspace containing the WMTS stores. | 
 **store** | **str**| The name of the store to be retrieved | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_stores**
> put_wmts_stores()



Invalid. Use POST for adding a new WMTS store, or PUT on /workspaces/{workspace}/wmtsstores/{wmtsstore} to edit an existing WMTS store.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_wmtsstores
from gs_rest_api_wmtsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmtsstores.DefaultApi()

try:
    api_instance.put_wmts_stores()
except ApiException as e:
    print("Exception when calling DefaultApi->put_wmts_stores: %s\n" % e)
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


# gs_rest_api_owsservices.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wcs_settings**](DefaultApi.md#delete_wcs_settings) | **DELETE** /services/wcs/settings | 
[**delete_wcs_workspace_settings**](DefaultApi.md#delete_wcs_workspace_settings) | **DELETE** /services/wcs/workspaces/{workspace}/settings | 
[**delete_wfs_settings**](DefaultApi.md#delete_wfs_settings) | **DELETE** /services/wfs/settings | 
[**delete_wfs_workspace_settings**](DefaultApi.md#delete_wfs_workspace_settings) | **DELETE** /services/wfs/workspaces/{workspace}/settings | 
[**delete_wms_settings**](DefaultApi.md#delete_wms_settings) | **DELETE** /services/wms/settings | 
[**delete_wms_workspace_settings**](DefaultApi.md#delete_wms_workspace_settings) | **DELETE** /services/wms/workspaces/{workspace}/settings | 
[**delete_wmts_settings**](DefaultApi.md#delete_wmts_settings) | **DELETE** /services/wmts/settings | 
[**delete_wmts_workspace_settings**](DefaultApi.md#delete_wmts_workspace_settings) | **DELETE** /services/wmts/workspaces/{workspace}/settings | 
[**get_wcs_settings**](DefaultApi.md#get_wcs_settings) | **GET** /services/wcs/settings | 
[**get_wcs_workspace_settings**](DefaultApi.md#get_wcs_workspace_settings) | **GET** /services/wcs/workspaces/{workspace}/settings | 
[**get_wfs_settings**](DefaultApi.md#get_wfs_settings) | **GET** /services/wfs/settings | 
[**get_wfs_workspace_settings**](DefaultApi.md#get_wfs_workspace_settings) | **GET** /services/wfs/workspaces/{workspace}/settings | 
[**get_wms_settings**](DefaultApi.md#get_wms_settings) | **GET** /services/wms/settings | 
[**get_wms_workspace_settings**](DefaultApi.md#get_wms_workspace_settings) | **GET** /services/wms/workspaces/{workspace}/settings | 
[**get_wmts_settings**](DefaultApi.md#get_wmts_settings) | **GET** /services/wmts/settings | 
[**get_wmts_workspace_settings**](DefaultApi.md#get_wmts_workspace_settings) | **GET** /services/wmts/workspaces/{workspace}/settings | 
[**post_wcs_settings**](DefaultApi.md#post_wcs_settings) | **POST** /services/wcs/settings | 
[**post_wcs_workspace_settings**](DefaultApi.md#post_wcs_workspace_settings) | **POST** /services/wcs/workspaces/{workspace}/settings | 
[**post_wfs_settings**](DefaultApi.md#post_wfs_settings) | **POST** /services/wfs/settings | 
[**post_wfs_workspace_settings**](DefaultApi.md#post_wfs_workspace_settings) | **POST** /services/wfs/workspaces/{workspace}/settings | 
[**post_wms_settings**](DefaultApi.md#post_wms_settings) | **POST** /services/wms/settings | 
[**post_wms_workspace_settings**](DefaultApi.md#post_wms_workspace_settings) | **POST** /services/wms/workspaces/{workspace}/settings | 
[**post_wmts_settings**](DefaultApi.md#post_wmts_settings) | **POST** /services/wmts/settings | 
[**post_wmts_workspace_settings**](DefaultApi.md#post_wmts_workspace_settings) | **POST** /services/wmts/workspaces/{workspace}/settings | 
[**put_wcs_settings**](DefaultApi.md#put_wcs_settings) | **PUT** /services/wcs/settings | 
[**put_wcs_workspace_settings**](DefaultApi.md#put_wcs_workspace_settings) | **PUT** /services/wcs/workspaces/{workspace}/settings | 
[**put_wfs_settings**](DefaultApi.md#put_wfs_settings) | **PUT** /services/wfs/settings | 
[**put_wfs_workspace_settings**](DefaultApi.md#put_wfs_workspace_settings) | **PUT** /services/wfs/workspaces/{workspace}/settings | 
[**put_wms_settings**](DefaultApi.md#put_wms_settings) | **PUT** /services/wms/settings | 
[**put_wms_workspace_settings**](DefaultApi.md#put_wms_workspace_settings) | **PUT** /services/wms/workspaces/{workspace}/settings | 
[**put_wmts_settings**](DefaultApi.md#put_wmts_settings) | **PUT** /services/wmts/settings | 
[**put_wmts_workspace_settings**](DefaultApi.md#put_wmts_workspace_settings) | **PUT** /services/wmts/workspaces/{workspace}/settings | 

# **delete_wcs_settings**
> delete_wcs_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.delete_wcs_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wcs_settings: %s\n" % e)
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

# **delete_wcs_workspace_settings**
> delete_wcs_workspace_settings(workspace)



Deletes a workspace-specific WCS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wcs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wfs_settings**
> delete_wfs_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.delete_wfs_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wfs_settings: %s\n" % e)
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

# **delete_wfs_workspace_settings**
> delete_wfs_workspace_settings(workspace)



Deletes a workspace-specific WFS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wfs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wms_settings**
> delete_wms_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.delete_wms_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_settings: %s\n" % e)
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

# **delete_wms_workspace_settings**
> delete_wms_workspace_settings(workspace)



Deletes a workspace-specific WMS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wms_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wmts_settings**
> delete_wmts_settings()



Invalid. Use PUT to edit settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.delete_wmts_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wmts_settings: %s\n" % e)
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

# **delete_wmts_workspace_settings**
> delete_wmts_workspace_settings(workspace)



Deletes a workspace-specific WMTS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_wmts_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wcs_settings**
> WCSInfo get_wcs_settings()



Retrieves Web Coverage Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_response = api_instance.get_wcs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wcs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WCSInfo**](WCSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wcs_workspace_settings**
> WCSInfo get_wcs_workspace_settings(workspace)



Retrieves Web Coverage Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wcs_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WCSInfo**](WCSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wfs_settings**
> WFSInfo get_wfs_settings()



Retrieves Web Feature Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_response = api_instance.get_wfs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wfs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WFSInfo**](WFSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wfs_workspace_settings**
> WFSInfo get_wfs_workspace_settings(workspace)



Retrieves Web Feature Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wfs_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WFSInfo**](WFSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_settings**
> WMSInfo get_wms_settings()



Retrieves Web Map Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_response = api_instance.get_wms_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMSInfo**](WMSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wms_workspace_settings**
> WMSInfo get_wms_workspace_settings(workspace)



Retrieves Web Map Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wms_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMSInfo**](WMSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_settings**
> WMTSInfo get_wmts_settings()



Retrieves Web Map Tile Service settings globally for the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_response = api_instance.get_wmts_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wmts_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WMTSInfo**](WMTSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wmts_workspace_settings**
> WMTSInfo get_wmts_workspace_settings(workspace)



Retrieves Web Map Tile Service settings for a given workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_response = api_instance.get_wmts_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WMTSInfo**](WMTSInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wcs_settings**
> post_wcs_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.post_wcs_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wcs_settings: %s\n" % e)
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

# **post_wcs_workspace_settings**
> post_wcs_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wcs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wfs_settings**
> post_wfs_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.post_wfs_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wfs_settings: %s\n" % e)
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

# **post_wfs_workspace_settings**
> post_wfs_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wfs_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wms_settings**
> post_wms_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.post_wms_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_settings: %s\n" % e)
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

# **post_wms_workspace_settings**
> post_wms_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wms_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wmts_settings**
> post_wmts_settings()



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()

try:
    api_instance.post_wmts_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wmts_settings: %s\n" % e)
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

# **post_wmts_workspace_settings**
> post_wmts_workspace_settings(workspace)



Invalid. Use PUT to edit a service setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.post_wmts_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wcs_settings**
> put_wcs_settings(body)



Edits a global WCS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WCSInfo() # WCSInfo | Body of the WCS settings

try:
    api_instance.put_wcs_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wcs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WCSInfo**](WCSInfo.md)| Body of the WCS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wcs_workspace_settings**
> put_wcs_workspace_settings(body, workspace)



Edits a workspace-specific WCS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WCSInfo() # WCSInfo | Body of the WCS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.put_wcs_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wcs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WCSInfo**](WCSInfo.md)| Body of the WCS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wfs_settings**
> put_wfs_settings(body)



Edits a global WFS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WFSInfo() # WFSInfo | Body of the WFS settings

try:
    api_instance.put_wfs_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WFSInfo**](WFSInfo.md)| Body of the WFS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wfs_workspace_settings**
> put_wfs_workspace_settings(body, workspace)



Edits a workspace-specific WFS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WFSInfo() # WFSInfo | Body of the WFS settings layer
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.put_wfs_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wfs_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WFSInfo**](WFSInfo.md)| Body of the WFS settings layer | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_settings**
> put_wms_settings(body)



Edits a global WMS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WMSInfo() # WMSInfo | Body of the WMS settings

try:
    api_instance.put_wms_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSInfo**](WMSInfo.md)| Body of the WMS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wms_workspace_settings**
> put_wms_workspace_settings(body, workspace)



Edits a workspace-specific WMS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WMSInfo() # WMSInfo | Body of the WMS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.put_wms_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMSInfo**](WMSInfo.md)| Body of the WMS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_settings**
> put_wmts_settings(body)



Edits a global WMTS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WMTSInfo() # WMTSInfo | Body of the WMTS settings

try:
    api_instance.put_wmts_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wmts_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSInfo**](WMTSInfo.md)| Body of the WMTS settings | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_wmts_workspace_settings**
> put_wmts_workspace_settings(body, workspace)



Edits a workspace-specific WMTS setting.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_owsservices
from gs_rest_api_owsservices.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_owsservices.DefaultApi()
body = gs_rest_api_owsservices.WMTSInfo() # WMTSInfo | Body of the WMTS settings
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.put_wmts_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wmts_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WMTSInfo**](WMTSInfo.md)| Body of the WMTS settings | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


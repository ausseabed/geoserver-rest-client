# gs_rest_api_layergroups.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_layergroup**](DefaultApi.md#delete_layergroup) | **DELETE** /layergroups/{layergroupName} | Delete layer group
[**delete_layergroups**](DefaultApi.md#delete_layergroups) | **DELETE** /layergroups | 
[**delete_workspace_layergroup**](DefaultApi.md#delete_workspace_layergroup) | **DELETE** /workspaces/{workspace}/layergroups/{layergroup} | Delete layer group
[**delete_workspace_layergroups**](DefaultApi.md#delete_workspace_layergroups) | **DELETE** /workspaces/{workspace}/layergroups | 
[**get_layergroup**](DefaultApi.md#get_layergroup) | **GET** /layergroups/{layergroupName} | Retrieve a layer group
[**get_layergroups**](DefaultApi.md#get_layergroups) | **GET** /layergroups | Get a list of layer groups
[**get_workspace_layergroup**](DefaultApi.md#get_workspace_layergroup) | **GET** /workspaces/{workspace}/layergroups/{layergroup} | Retrieve a layer group
[**get_workspace_layergroups**](DefaultApi.md#get_workspace_layergroups) | **GET** /workspaces/{workspace}/layergroups | Get a list of layer groups in a workspace
[**post_layergroup**](DefaultApi.md#post_layergroup) | **POST** /layergroups/{layergroupName} | 
[**post_layergroups**](DefaultApi.md#post_layergroups) | **POST** /layergroups | Add a new layer group
[**post_workspace_layergroup**](DefaultApi.md#post_workspace_layergroup) | **POST** /workspaces/{workspace}/layergroups/{layergroup} | 
[**post_workspace_layergroups**](DefaultApi.md#post_workspace_layergroups) | **POST** /workspaces/{workspace}/layergroups | Add a new layer group
[**put_layergroup**](DefaultApi.md#put_layergroup) | **PUT** /layergroups/{layergroupName} | Modify a layer group.
[**put_layergroups**](DefaultApi.md#put_layergroups) | **PUT** /layergroups | 
[**put_workspace_layergroup**](DefaultApi.md#put_workspace_layergroup) | **PUT** /workspaces/{workspace}/layergroups/{layergroup} | Modify a layer group.
[**put_workspace_layergroups**](DefaultApi.md#put_workspace_layergroups) | **PUT** /workspaces/{workspace}/layergroups | 

# **delete_layergroup**
> delete_layergroup(layergroup_name)

Delete layer group

Deletes a layer group from the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to delete.

try:
    # Delete layer group
    api_instance.delete_layergroup(layergroup_name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_name** | **str**| The name of the layer group to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_layergroups**
> delete_layergroups()



Invalid. Use /layergroups/{layergroup} instead.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.delete_layergroups()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_layergroups: %s\n" % e)
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

# **delete_workspace_layergroup**
> delete_workspace_layergroup(layergroup, workspace)

Delete layer group

Deletes a layer group from the server in the given workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
layergroup = 'layergroup_example' # str | The name of the layer group to delete.
workspace = 'workspace_example' # str | The name of the workspace

try:
    # Delete layer group
    api_instance.delete_workspace_layergroup(layergroup, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup** | **str**| The name of the layer group to delete. | 
 **workspace** | **str**| The name of the workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_layergroups**
> delete_workspace_layergroups()



Invalid. Use /workspaces/{workspace}/layergroups/{layergroup} instead.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.delete_workspace_layergroups()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_workspace_layergroups: %s\n" % e)
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

# **get_layergroup**
> LayergroupWrapper get_layergroup(layergroup_name)

Retrieve a layer group

Retrieves a single layer group definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to retrieve.

try:
    # Retrieve a layer group
    api_response = api_instance.get_layergroup(layergroup_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layergroup_name** | **str**| The name of the layer group to retrieve. | 

### Return type

[**LayergroupWrapper**](LayergroupWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_layergroups**
> LayergroupResponse get_layergroups()

Get a list of layer groups

Displays a list of all layer groups on the server not otherwise in a workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    # Get a list of layer groups
    api_response = api_instance.get_layergroups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_layergroups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LayergroupResponse**](LayergroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_layergroup**
> LayergroupWrapper get_workspace_layergroup(workspace, layergroup)

Retrieve a layer group

Retrieves a single layer group definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
layergroup = 'layergroup_example' # str | The name of the layer group to retrieve.

try:
    # Retrieve a layer group
    api_response = api_instance.get_workspace_layergroup(workspace, layergroup)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **layergroup** | **str**| The name of the layer group to retrieve. | 

### Return type

[**LayergroupWrapper**](LayergroupWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_layergroups**
> LayergroupResponse get_workspace_layergroups(workspace)

Get a list of layer groups in a workspace

Displays a list of all layer groups in a given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace

try:
    # Get a list of layer groups in a workspace
    api_response = api_instance.get_workspace_layergroups(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workspace_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 

### Return type

[**LayergroupResponse**](LayergroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_layergroup**
> post_layergroup()



Invalid. Use PUT to edit a layer group definition, or POST with /layergroups to add a new definition.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.post_layergroup()
except ApiException as e:
    print("Exception when calling DefaultApi->post_layergroup: %s\n" % e)
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

# **post_layergroups**
> str post_layergroups(body)

Add a new layer group

Adds a new layer group entry to the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
body = gs_rest_api_layergroups.LayergroupWrapper() # LayergroupWrapper | The layer group body information to upload.

try:
    # Add a new layer group
    api_response = api_instance.post_layergroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayergroupWrapper**](LayergroupWrapper.md)| The layer group body information to upload. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_layergroup**
> post_workspace_layergroup()



Invalid. Use PUT to edit a layer group definition, or POST with /workspaces/{workspace}/layergroups to add a new definition.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.post_workspace_layergroup()
except ApiException as e:
    print("Exception when calling DefaultApi->post_workspace_layergroup: %s\n" % e)
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

# **post_workspace_layergroups**
> str post_workspace_layergroups(body)

Add a new layer group

Adds a new layer group entry to the server in the specified workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
body = gs_rest_api_layergroups.LayergroupWrapper() # LayergroupWrapper | The layer group body information to upload.

try:
    # Add a new layer group
    api_response = api_instance.post_workspace_layergroups(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_workspace_layergroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayergroupWrapper**](LayergroupWrapper.md)| The layer group body information to upload. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_layergroup**
> put_layergroup(body, layergroup_name)

Modify a layer group.

Modifies an existing layer group on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
body = gs_rest_api_layergroups.LayergroupWrapper() # LayergroupWrapper | The updated layer group definition.
layergroup_name = 'layergroup_name_example' # str | The name of the layer group to modify.

try:
    # Modify a layer group.
    api_instance.put_layergroup(body, layergroup_name)
except ApiException as e:
    print("Exception when calling DefaultApi->put_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayergroupWrapper**](LayergroupWrapper.md)| The updated layer group definition. | 
 **layergroup_name** | **str**| The name of the layer group to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_layergroups**
> put_layergroups()



Invalid. Use POST for adding a new layer group, or PUT on /layergroups/{layergroup} to edit an existing layer group.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.put_layergroups()
except ApiException as e:
    print("Exception when calling DefaultApi->put_layergroups: %s\n" % e)
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

# **put_workspace_layergroup**
> put_workspace_layergroup(body, workspace, layergroup)

Modify a layer group.

Modifies an existing layer group on the server in the given workspace. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/workspaces/{workspace}/layergroups/{layergroup}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()
body = gs_rest_api_layergroups.LayergroupWrapper() # LayergroupWrapper | The updated layer group definition.
workspace = 'workspace_example' # str | The name of the workspace
layergroup = 'layergroup_example' # str | The name of the layer group to modify.

try:
    # Modify a layer group.
    api_instance.put_workspace_layergroup(body, workspace, layergroup)
except ApiException as e:
    print("Exception when calling DefaultApi->put_workspace_layergroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LayergroupWrapper**](LayergroupWrapper.md)| The updated layer group definition. | 
 **workspace** | **str**| The name of the workspace | 
 **layergroup** | **str**| The name of the layer group to modify. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_layergroups**
> put_workspace_layergroups()



Invalid. Use POST for adding a new layer group to a workspace, or PUT on /workspaces/{workspace}/layergroups/{layergroup} to edit an existing layer group.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_layergroups
from gs_rest_api_layergroups.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layergroups.DefaultApi()

try:
    api_instance.put_workspace_layergroups()
except ApiException as e:
    print("Exception when calling DefaultApi->put_workspace_layergroups: %s\n" % e)
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


# gs_rest_api_coverages.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_coverage**](DefaultApi.md#delete_coverage) | **DELETE** /workspaces/{workspace}/coverages/{coverage} | 
[**delete_coverage_store**](DefaultApi.md#delete_coverage_store) | **DELETE** /workspaces/{workspace}/coverages | 
[**delete_workspace_coverage**](DefaultApi.md#delete_workspace_coverage) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**delete_workspace_coverage_store**](DefaultApi.md#delete_workspace_coverage_store) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**get_coverage**](DefaultApi.md#get_coverage) | **GET** /workspaces/{workspace}/coverages/{coverage} | 
[**get_coverage_store**](DefaultApi.md#get_coverage_store) | **GET** /workspaces/{workspace}/coverages | 
[**get_workspace_coverage**](DefaultApi.md#get_workspace_coverage) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**get_workspace_coverage_store**](DefaultApi.md#get_workspace_coverage_store) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**post_coverage**](DefaultApi.md#post_coverage) | **POST** /workspaces/{workspace}/coverages/{coverage} | 
[**post_coverage_store**](DefaultApi.md#post_coverage_store) | **POST** /workspaces/{workspace}/coverages | 
[**post_workspace_coverage**](DefaultApi.md#post_workspace_coverage) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**post_workspace_coverage_store**](DefaultApi.md#post_workspace_coverage_store) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages | 
[**put_coverage**](DefaultApi.md#put_coverage) | **PUT** /workspaces/{workspace}/coverages/{coverage} | 
[**put_coverage_store**](DefaultApi.md#put_coverage_store) | **PUT** /workspaces/{workspace}/coverages | 
[**put_workspace_coverage**](DefaultApi.md#put_workspace_coverage) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage} | 
[**put_workspace_coverage_store**](DefaultApi.md#put_workspace_coverage_store) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages | 

# **delete_coverage**
> delete_coverage()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.delete_coverage()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_coverage: %s\n" % e)
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

# **delete_coverage_store**
> delete_coverage_store()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.delete_coverage_store()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_coverage_store: %s\n" % e)
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

# **delete_workspace_coverage**
> delete_workspace_coverage(workspace, store, coverage, recurse=recurse)



Delete a coverage (optionally recursively deleting layers).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
coverage = 'coverage_example' # str | The name of the coverage
recurse = true # bool | The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. (optional)

try:
    api_instance.delete_workspace_coverage(workspace, store, coverage, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **coverage** | **str**| The name of the coverage | 
 **recurse** | **bool**| The recurse controls recursive deletion. When set to true all stores containing the resource are also removed. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_coverage_store**
> delete_workspace_coverage_store()



Invalid. Can only delete an individual coverage.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.delete_workspace_coverage_store()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_workspace_coverage_store: %s\n" % e)
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

# **get_coverage**
> object get_coverage(workspace, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = true # bool | The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional)

try:
    api_response = api_instance.get_coverage(workspace, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coverage_store**
> object get_coverage_store(workspace, list=list)



Get the coverages available for the provided workspace. 

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non published ones) will be returned.  (optional)

try:
    api_response = api_instance.get_coverage_store(workspace, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non published ones) will be returned.  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_coverage**
> object get_workspace_coverage(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)



Get an individual coverage.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage datastore
coverage = 'coverage_example' # str | The name of the coverage
quiet_on_not_found = true # bool | The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. (optional)

try:
    api_response = api_instance.get_workspace_coverage(workspace, store, coverage, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage datastore | 
 **coverage** | **str**| The name of the coverage | 
 **quiet_on_not_found** | **bool**| The quietOnNotFound parameter avoids to log an Exception when the coverage is not present. Note that 404 status code will be returned anyway. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_coverage_store**
> object get_workspace_coverage_store(workspace, store, list=list)



Get the coverages available for the provided workspace and data store. 

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
list = 'list_example' # str | If the list parameter value is equal to \"all\" all the coverages available in the data source (even the non published ones) will be returned.  (optional)

try:
    api_response = api_instance.get_workspace_coverage_store(workspace, store, list=list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workspace_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **list** | **str**| If the list parameter value is equal to \&quot;all\&quot; all the coverages available in the data source (even the non published ones) will be returned.  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_coverage**
> post_coverage()



Invalid. Use POST on the coverages endpoint to add a new coverage, or PUT on an individual coverage to edit it.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.post_coverage()
except ApiException as e:
    print("Exception when calling DefaultApi->post_coverage: %s\n" % e)
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

# **post_coverage_store**
> post_coverage_store(body, workspace)



Create a new coverage, the coverage definition needs to reference a store. 

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
body = gs_rest_api_coverages.CoverageInfo() # CoverageInfo | The body of the coverage to POST
workspace = 'workspace_example' # str | The name of the workspace

try:
    api_instance.post_coverage_store(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to POST | 
 **workspace** | **str**| The name of the workspace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workspace_coverage**
> post_workspace_coverage()



Invalid. Use POST on the coverages endpoint to add a new coverage, or PUT on an individual coverage to edit it.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.post_workspace_coverage()
except ApiException as e:
    print("Exception when calling DefaultApi->post_workspace_coverage: %s\n" % e)
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

# **post_workspace_coverage_store**
> post_workspace_coverage_store(body, workspace, store)



Create a new coverage, the underlying data store must exists. 

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
body = gs_rest_api_coverages.CoverageInfo() # CoverageInfo | The body of the coverage to POST
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store

try:
    api_instance.post_workspace_coverage_store(body, workspace, store)
except ApiException as e:
    print("Exception when calling DefaultApi->post_workspace_coverage_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to POST | 
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_coverage**
> put_coverage()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.put_coverage()
except ApiException as e:
    print("Exception when calling DefaultApi->put_coverage: %s\n" % e)
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

# **put_coverage_store**
> put_coverage_store()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.put_coverage_store()
except ApiException as e:
    print("Exception when calling DefaultApi->put_coverage_store: %s\n" % e)
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

# **put_workspace_coverage**
> put_workspace_coverage(body, workspace, store, coverage, calculate=calculate)



Update an individual coverage

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()
body = gs_rest_api_coverages.CoverageInfo() # CoverageInfo | The body of the coverage to PUT
workspace = 'workspace_example' # str | The name of the workspace
store = 'store_example' # str | The name of the coverage data store
coverage = 'coverage_example' # str | The name of the coverage
calculate = ['calculate_example'] # list[str] | Comma-seperated list of optional fields to calculate. Optional fields include: \"nativebbox\", \"latlonbbox\". (optional)

try:
    api_instance.put_workspace_coverage(body, workspace, store, coverage, calculate=calculate)
except ApiException as e:
    print("Exception when calling DefaultApi->put_workspace_coverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CoverageInfo**](CoverageInfo.md)| The body of the coverage to PUT | 
 **workspace** | **str**| The name of the workspace | 
 **store** | **str**| The name of the coverage data store | 
 **coverage** | **str**| The name of the coverage | 
 **calculate** | [**list[str]**](str.md)| Comma-seperated list of optional fields to calculate. Optional fields include: \&quot;nativebbox\&quot;, \&quot;latlonbbox\&quot;. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_coverage_store**
> put_workspace_coverage_store()



Invalid. Use POST for adding a new coverage, or PUT on an individual coverage to edit that type.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_coverages
from gs_rest_api_coverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_coverages.DefaultApi()

try:
    api_instance.put_workspace_coverage_store()
except ApiException as e:
    print("Exception when calling DefaultApi->put_workspace_coverage_store: %s\n" % e)
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


# gs_rest_api_importerTransforms.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_transform**](DefaultApi.md#delete_transform) | **DELETE** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Removes the transformation
[**get_transform**](DefaultApi.md#get_transform) | **GET** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Retrieve a transformation
[**get_transforms**](DefaultApi.md#get_transforms) | **GET** /imports/{importId}/tasks/{taskId}/transforms | Retrieve transformation list
[**post_transform**](DefaultApi.md#post_transform) | **POST** /imports/{importId}/tasks/{taskId}/transforms | Create a new transformation
[**put_transform**](DefaultApi.md#put_transform) | **PUT** /imports/{importId}/tasks/{taskId}/transforms/{transformId} | Modifies a transformation

# **delete_transform**
> delete_transform(import_id, task_id, transform_id)

Removes the transformation

Removes the transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTransforms
from gs_rest_api_importerTransforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTransforms.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform

try:
    # Removes the transformation
    api_instance.delete_transform(import_id, task_id, transform_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transform**
> Transform get_transform(import_id, task_id, transform_id, expand=expand)

Retrieve a transformation

Retrieve a transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTransforms
from gs_rest_api_importerTransforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTransforms.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Retrieve a transformation
    api_response = api_instance.get_transform(import_id, task_id, transform_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transforms**
> Transforms get_transforms(import_id, task_id, expand=expand)

Retrieve transformation list

Retrieve the list of transformations of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTransforms
from gs_rest_api_importerTransforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTransforms.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Retrieve transformation list
    api_response = api_instance.get_transforms(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transforms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transforms**](Transforms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_transform**
> post_transform(body, import_id, task_id, expand=expand)

Create a new transformation

Create a new transormation and append it inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTransforms
from gs_rest_api_importerTransforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTransforms.DefaultApi()
body = gs_rest_api_importerTransforms.Transform() # Transform | The transform to add.
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Create a new transformation
    api_instance.post_transform(body, import_id, task_id, expand=expand)
except ApiException as e:
    print("Exception when calling DefaultApi->post_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transform**](Transform.md)| The transform to add. | 
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_transform**
> Transform put_transform(body, import_id, task_id, transform_id, expand=expand)

Modifies a transformation

Modifies the definition of a transformation identified by {transformId} inside a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTransforms
from gs_rest_api_importerTransforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTransforms.DefaultApi()
body = gs_rest_api_importerTransforms.Transform() # Transform | The transform to add.
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
transform_id = 'transform_id_example' # str | The ID of the transform
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \"self\" or \"none\", depending on the request. (optional)

try:
    # Modifies a transformation
    api_response = api_instance.put_transform(body, import_id, task_id, transform_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_transform: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transform**](Transform.md)| The transform to add. | 
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **transform_id** | **str**| The ID of the transform | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. Defaults to \&quot;self\&quot; or \&quot;none\&quot;, depending on the request. | [optional] 

### Return type

[**Transform**](Transform.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


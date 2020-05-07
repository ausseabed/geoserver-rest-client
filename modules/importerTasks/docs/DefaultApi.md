# gs_rest_api_importerTasks.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task**](DefaultApi.md#delete_task) | **DELETE** /imports/{importId}/tasks/{taskId} | Remove task with id {taskId} within import with id {importId}
[**get_task**](DefaultApi.md#get_task) | **GET** /imports/{importId}/tasks/{taskId} | Retrieve task with id {taskId} within import with id {importId}
[**get_task_layer**](DefaultApi.md#get_task_layer) | **GET** /imports/{importId}/tasks/{taskId}/layer | Retrieve the layer of a task with id {taskId} within import with id {importId}
[**get_task_progress**](DefaultApi.md#get_task_progress) | **GET** /imports/{importId}/tasks/{taskId}/progress | Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}
[**get_task_target**](DefaultApi.md#get_task_target) | **GET** /imports/{importId}/tasks/{taskId}/target | Retrieve the store of a task with id {taskId} within import with id {importId}
[**get_tasks**](DefaultApi.md#get_tasks) | **GET** /imports/{importId}/tasks | Retrieve all tasks for import with id {importId}
[**post_task**](DefaultApi.md#post_task) | **POST** /imports/{importId}/tasks | Create a new task
[**put_task**](DefaultApi.md#put_task) | **PUT** /imports/{importId}/tasks/{taskId} | Modify task with id {taskId} within import with id {importId}
[**put_task_file**](DefaultApi.md#put_task_file) | **PUT** /imports/{importId}/tasks/{filename} | Create a new task
[**put_task_layer**](DefaultApi.md#put_task_layer) | **PUT** /imports/{importId}/tasks/{taskId}/layer | Modify the target layer for a task with id {taskId} within import with id {importId}
[**put_task_target**](DefaultApi.md#put_task_target) | **PUT** /imports/{importId}/tasks/{taskId}/target | Modify the target store for a task with id {taskId} within import with id {importId}

# **delete_task**
> delete_task(import_id, task_id)

Remove task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task

try:
    # Remove task with id {taskId} within import with id {importId}
    api_instance.delete_task(import_id, task_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task(import_id, task_id, expand=expand)

Retrieve task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Retrieve task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_layer**
> Layer get_task_layer(import_id, task_id, expand=expand)

Retrieve the layer of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Retrieve the layer of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_layer(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Layer**](Layer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_progress**
> Progress get_task_progress(import_id, task_id)

Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task

try:
    # Retrieve the current state and import progress of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_progress(import_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 

### Return type

[**Progress**](Progress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/htm

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_target**
> Store get_task_target(import_id, task_id, expand=expand)

Retrieve the store of a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Retrieve the store of a task with id {taskId} within import with id {importId}
    api_response = api_instance.get_task_target(import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_task_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Store**](Store.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> Tasks get_tasks(import_id, expand=expand)

Retrieve all tasks for import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Retrieve all tasks for import with id {importId}
    api_response = api_instance.get_tasks(import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task**
> Task post_task(id, href, state, update_mode, data, target, progress, layer, error_message, transform_chain, messages, import_id, expand=expand)

Create a new task

A new task can be created by issuing a POST to imports/<importId>/tasks as a \"Content-type: multipart/form-data\" multipart encoded data as defined by RFC 2388. One or more file can be uploaded this way, and a task will be created for importing them. In case the file being uploaded is a zip file, it will be unzipped on the server side and treated as a directory of files. Alternatively, a new task can be created by issuing a POST as a \"Content-type: application/x-www-form-urlencoded\" form url encoded data containing a url paramerter with the location of the uploaded file.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
id = 'id_example' # str | 
href = 'href_example' # str | 
state = 'state_example' # str | 
update_mode = 'update_mode_example' # str | 
data = gs_rest_api_importerTasks.Data() # Data | 
target = gs_rest_api_importerTasks.Store() # Store | 
progress = 'progress_example' # str | 
layer = gs_rest_api_importerTasks.Layer() # Layer | 
error_message = 'error_message_example' # str | 
transform_chain = gs_rest_api_importerTasks.TransformChain() # TransformChain | 
messages = gs_rest_api_importerTasks.Messages() # Messages | 
import_id = 'import_id_example' # str | The ID of the import
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Create a new task
    api_response = api_instance.post_task(id, href, state, update_mode, data, target, progress, layer, error_message, transform_chain, messages, import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **href** | **str**|  | 
 **state** | **str**|  | 
 **update_mode** | **str**|  | 
 **data** | [**Data**](.md)|  | 
 **target** | [**Store**](.md)|  | 
 **progress** | **str**|  | 
 **layer** | [**Layer**](.md)|  | 
 **error_message** | **str**|  | 
 **transform_chain** | [**TransformChain**](.md)|  | 
 **messages** | [**Messages**](.md)|  | 
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json, text/htm

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task**
> Task put_task(body, import_id, task_id, expand=expand)

Modify task with id {taskId} within import with id {importId}

A PUT request over an existing task can be used to update its representation. The representation can be partial, and just contains the elements that need to be updated. The updateMode of a task normally starts as \"CREATE\", that is, create the target resource if missing. Other possible values are \"REPLACE\", that is, delete the existing features in the target layer and replace them with the task source ones, or \"APPEND\", to just add the features from the task source into an existing layer.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
body = gs_rest_api_importerTasks.Task() # Task | The task to create or modify
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Modify task with id {taskId} within import with id {importId}
    api_response = api_instance.put_task(body, import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Task**](Task.md)| The task to create or modify | 
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_file**
> Tasks put_task_file(body, import_id, filename, expand=expand)

Create a new task

A new task can be created by issuing a PUT containing the raw file content to this endpoint. The name of the uploaded file will be {filename}. The location of the uploaded file will be the top level directory associated with the import, or the \"uploads\" directory in the data directory if no directory is associated with the current import.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
body = 'body_example' # str | The file contents to upload.
import_id = 'import_id_example' # str | The ID of the import
filename = 'filename_example' # str | The filename
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Create a new task
    api_response = api_instance.put_task_file(body, import_id, filename, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_task_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| The file contents to upload. | 
 **import_id** | **str**| The ID of the import | 
 **filename** | **str**| The filename | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: \\*/*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_layer**
> Task put_task_layer(body, import_id, task_id, expand=expand)

Modify the target layer for a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
body = gs_rest_api_importerTasks.Layer() # Layer | The layer to modify
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Modify the target layer for a task with id {taskId} within import with id {importId}
    api_response = api_instance.put_task_layer(body, import_id, task_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_task_layer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Layer**](Layer.md)| The layer to modify | 
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_target**
> put_task_target(body, import_id, task_id)

Modify the target store for a task with id {taskId} within import with id {importId}

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importerTasks
from gs_rest_api_importerTasks.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importerTasks.DefaultApi()
body = gs_rest_api_importerTasks.Store() # Store | The store to modify
import_id = 'import_id_example' # str | The ID of the import
task_id = 'task_id_example' # str | The ID of the task

try:
    # Modify the target store for a task with id {taskId} within import with id {importId}
    api_instance.put_task_target(body, import_id, task_id)
except ApiException as e:
    print("Exception when calling DefaultApi->put_task_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Store**](Store.md)| The store to modify | 
 **import_id** | **str**| The ID of the import | 
 **task_id** | **str**| The ID of the task | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


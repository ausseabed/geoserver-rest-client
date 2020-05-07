# gs_rest_api_importer.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_import**](DefaultApi.md#delete_import) | **DELETE** /imports/{importId} | Delete an import
[**delete_imports**](DefaultApi.md#delete_imports) | **DELETE** /imports | Delete all imports
[**get_import**](DefaultApi.md#get_import) | **GET** /imports/{importId} | Retrieve import by id
[**get_imports**](DefaultApi.md#get_imports) | **GET** /imports | Get a list of all imports
[**post_import**](DefaultApi.md#post_import) | **POST** /imports/{importId} | Create a new import, or execute an existing import
[**post_imports**](DefaultApi.md#post_imports) | **POST** /imports | Create a new import
[**put_import**](DefaultApi.md#put_import) | **PUT** /imports/{importId} | Tries to create a new import with the provided id.

# **delete_import**
> delete_import()

Delete an import

Deletes the import with id {importId}, as long as it is not in the COMPLETE state.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()

try:
    # Delete an import
    api_instance.delete_import()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_import: %s\n" % e)
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

# **delete_imports**
> delete_imports()

Delete all imports

Deletes all imports that are not in the COMPLETE state.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()

try:
    # Delete all imports
    api_instance.delete_imports()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_imports: %s\n" % e)
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

# **get_import**
> Context get_import(import_id, expand=expand)

Retrieve import by id

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()
import_id = 'import_id_example' # str | The ID of the import
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Retrieve import by id
    api_response = api_instance.get_import(import_id, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **str**| The ID of the import | 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Context**](Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_imports**
> Contexts get_imports(expand=expand)

Get a list of all imports

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Get a list of all imports
    api_response = api_instance.get_imports(expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_imports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Contexts**](Contexts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_import**
> Context post_import(body, _async=_async, _exec=_exec, expand=expand)

Create a new import, or execute an existing import

If an import with the id {importId} exists and is not in the INIT state, it is executed. If an import with that id does not exist, a new import is created with that id. If the exec parameter is true, this new import is immediately executed.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()
body = gs_rest_api_importer.Context() # Context | The import context to create.
_async = true # bool | Run the import asyncronously. (optional)
_exec = true # bool | Run the import when it is created. (optional)
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Create a new import, or execute an existing import
    api_response = api_instance.post_import(body, _async=_async, _exec=_exec, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Context**](Context.md)| The import context to create. | 
 **_async** | **bool**| Run the import asyncronously. | [optional] 
 **_exec** | **bool**| Run the import when it is created. | [optional] 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Context**](Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_imports**
> Context post_imports(body, _async=_async, _exec=_exec, expand=expand)

Create a new import

Creates a new import. If the exec parameter is true, that import is immediately executed.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()
body = gs_rest_api_importer.Context() # Context | The import context to create.
_async = true # bool | Run the import asyncronously. (optional)
_exec = true # bool | Run the import when it is created. (optional)
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Create a new import
    api_response = api_instance.post_imports(body, _async=_async, _exec=_exec, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_imports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Context**](Context.md)| The import context to create. | 
 **_async** | **bool**| Run the import asyncronously. | [optional] 
 **_exec** | **bool**| Run the import when it is created. | [optional] 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Context**](Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_import**
> Context put_import(body, _async=_async, _exec=_exec, expand=expand)

Tries to create a new import with the provided id.

Creates a new import with the next unclaimed id >= {importId}. If the exec parameter is true, that import is immediately executed.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_importer
from gs_rest_api_importer.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_importer.DefaultApi()
body = gs_rest_api_importer.Context() # Context | The import context to create.
_async = true # bool | Run the import asyncronously. (optional)
_exec = true # bool | Run the import when it is created. (optional)
expand = 'expand_example' # str | What level to expand the response object to. Can be \"self\" (expand only the response object and its immediate children), \"all\" (expand all children), \"none\" (don't include any children), or a nonnegative integer, indicating the depth of children to expand to. (optional)

try:
    # Tries to create a new import with the provided id.
    api_response = api_instance.put_import(body, _async=_async, _exec=_exec, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Context**](Context.md)| The import context to create. | 
 **_async** | **bool**| Run the import asyncronously. | [optional] 
 **_exec** | **bool**| Run the import when it is created. | [optional] 
 **expand** | **str**| What level to expand the response object to. Can be \&quot;self\&quot; (expand only the response object and its immediate children), \&quot;all\&quot; (expand all children), \&quot;none\&quot; (don&#x27;t include any children), or a nonnegative integer, indicating the depth of children to expand to. | [optional] 

### Return type

[**Context**](Context.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


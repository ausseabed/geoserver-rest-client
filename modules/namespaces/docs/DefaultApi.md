# gs_rest_api_namespaces.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_namespace**](DefaultApi.md#delete_namespace) | **DELETE** /namespaces/{namespaceName} | Delete a namespace
[**delete_namespaces**](DefaultApi.md#delete_namespaces) | **DELETE** /namespaces | 
[**get_namespace**](DefaultApi.md#get_namespace) | **GET** /namespaces/{namespaceName} | Retrieve a namespace
[**get_namespaces**](DefaultApi.md#get_namespaces) | **GET** /namespaces | Get a list of namespaces
[**post_namespace**](DefaultApi.md#post_namespace) | **POST** /namespaces/{namespaceName} | 
[**post_namespaces**](DefaultApi.md#post_namespaces) | **POST** /namespaces | Add a new namespace to GeoServer
[**put_namespace**](DefaultApi.md#put_namespace) | **PUT** /namespaces/{namespaceName} | Update a namespace
[**put_namespaces**](DefaultApi.md#put_namespaces) | **PUT** /namespaces | 

# **delete_namespace**
> delete_namespace(namespace_name)

Delete a namespace

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()
namespace_name = 'namespace_name_example' # str | Name of the namespace

try:
    # Delete a namespace
    api_instance.delete_namespace(namespace_name)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| Name of the namespace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaces**
> delete_namespaces()



### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()

try:
    api_instance.delete_namespaces()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_namespaces: %s\n" % e)
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

# **get_namespace**
> NamespaceResponse get_namespace(namespace_name)

Retrieve a namespace

Retrieves a single namespace definition. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces/{namespace}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()
namespace_name = 'namespace_name_example' # str | The name of the namespace to fetch, or \"default\" to get the default namespace.

try:
    # Retrieve a namespace
    api_response = api_instance.get_namespace(namespace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| The name of the namespace to fetch, or \&quot;default\&quot; to get the default namespace. | 

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces**
> NamespacesResponse get_namespaces()

Get a list of namespaces

Displays a list of all namespaces on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/namespaces.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()

try:
    # Get a list of namespaces
    api_response = api_instance.get_namespaces()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_namespaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NamespacesResponse**](NamespacesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_namespace**
> post_namespace()



### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()

try:
    api_instance.post_namespace()
except ApiException as e:
    print("Exception when calling DefaultApi->post_namespace: %s\n" % e)
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

# **post_namespaces**
> str post_namespaces(body)

Add a new namespace to GeoServer

Adds a new namespace to the server

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()
body = gs_rest_api_namespaces.Namespace() # Namespace | The layer group body information to upload.

try:
    # Add a new namespace to GeoServer
    api_response = api_instance.post_namespaces(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Namespace**](Namespace.md)| The layer group body information to upload. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: text/html, application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespace**
> put_namespace(namespace_name)

Update a namespace

Takes the body of the put and modifies the namespace from it.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()
namespace_name = 'namespace_name_example' # str | Name of namespace, or \"default\" to set the default namespace using the namespace prefix in the body of the post.

try:
    # Update a namespace
    api_instance.put_namespace(namespace_name)
except ApiException as e:
    print("Exception when calling DefaultApi->put_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| Name of namespace, or \&quot;default\&quot; to set the default namespace using the namespace prefix in the body of the post. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_namespaces**
> put_namespaces()



### Example
```python
from __future__ import print_function
import time
import gs_rest_api_namespaces
from gs_rest_api_namespaces.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_namespaces.DefaultApi()

try:
    api_instance.put_namespaces()
except ApiException as e:
    print("Exception when calling DefaultApi->put_namespaces: %s\n" % e)
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


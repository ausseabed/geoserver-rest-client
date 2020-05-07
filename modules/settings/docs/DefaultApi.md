# gs_rest_api_settings.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact_settings**](DefaultApi.md#delete_contact_settings) | **DELETE** /settings/contact | 
[**delete_settings**](DefaultApi.md#delete_settings) | **DELETE** /settings | 
[**delete_workspace_settings**](DefaultApi.md#delete_workspace_settings) | **DELETE** /workspaces/{workspace}/settings | 
[**get_contact_settings**](DefaultApi.md#get_contact_settings) | **GET** /settings/contact | Get a list of all global contact settings
[**get_settings**](DefaultApi.md#get_settings) | **GET** /settings | Get a list of all global settings
[**get_workspace_settings**](DefaultApi.md#get_workspace_settings) | **GET** /workspaces/{workspace}/settings | Get a list of all workspace-specific settings
[**post_contact_settings**](DefaultApi.md#post_contact_settings) | **POST** /settings/contact | 
[**post_settings**](DefaultApi.md#post_settings) | **POST** /settings | 
[**post_workspace_settings**](DefaultApi.md#post_workspace_settings) | **POST** /workspaces/{workspace}/settings | Create workspace-specific settings
[**put_contact_settings**](DefaultApi.md#put_contact_settings) | **PUT** /settings/contact | Update contact settings
[**put_settings**](DefaultApi.md#put_settings) | **PUT** /settings | Update settings
[**put_workspace_settings**](DefaultApi.md#put_workspace_settings) | **PUT** /workspaces/{workspace}/settings | Update workspace-specific settings

# **delete_contact_settings**
> delete_contact_settings()



Invalid. Use PUT to update contact settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    api_instance.delete_contact_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_contact_settings: %s\n" % e)
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

# **delete_settings**
> delete_settings()



Invalid. Use PUT to update settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    api_instance.delete_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_settings: %s\n" % e)
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

# **delete_workspace_settings**
> delete_workspace_settings(workspace)



Delete the settings for this workspace.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    api_instance.delete_workspace_settings(workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_workspace_settings: %s\n" % e)
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

# **get_contact_settings**
> Contact get_contact_settings()

Get a list of all global contact settings

Displays a list of all global contact settings on the server. This is a subset of what is available at the /settings endpoint. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/settings/contact.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    # Get a list of all global contact settings
    api_response = api_instance.get_contact_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_contact_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ModelGlobal get_settings()

Get a list of all global settings

Displays a list of all global settings on the server. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/settings.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    # Get a list of all global settings
    api_response = api_instance.get_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelGlobal**](ModelGlobal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_settings**
> WorkspaceSettings get_workspace_settings(workspace)

Get a list of all workspace-specific settings

Displays a list of all workspace-specific settings. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/settings.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
workspace = 'workspace_example' # str | The workspace name

try:
    # Get a list of all workspace-specific settings
    api_response = api_instance.get_workspace_settings(workspace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace** | **str**| The workspace name | 

### Return type

[**WorkspaceSettings**](WorkspaceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_contact_settings**
> post_contact_settings()



Invalid. Use PUT to update contact settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    api_instance.post_contact_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_contact_settings: %s\n" % e)
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

# **post_settings**
> post_settings()



Invalid. Use PUT to update settings.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()

try:
    api_instance.post_settings()
except ApiException as e:
    print("Exception when calling DefaultApi->post_settings: %s\n" % e)
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

# **post_workspace_settings**
> post_workspace_settings(body, workspace)

Create workspace-specific settings

Create new workspace-specific settings on the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
body = gs_rest_api_settings.WorkspaceSettings() # WorkspaceSettings | The settings information to upload.
workspace = 'workspace_example' # str | The workspace name

try:
    # Create workspace-specific settings
    api_instance.post_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceSettings**](WorkspaceSettings.md)| The settings information to upload. | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_contact_settings**
> put_contact_settings(body)

Update contact settings

Updates global contact settings on the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
body = gs_rest_api_settings.Contact() # Contact | The contact settings information to upload.

try:
    # Update contact settings
    api_instance.put_contact_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_contact_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Contact**](Contact.md)| The contact settings information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_settings**
> put_settings(body)

Update settings

Updates global settings on the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
body = gs_rest_api_settings.ModelGlobal() # ModelGlobal | The settings information to upload.

try:
    # Update settings
    api_instance.put_settings(body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelGlobal**](ModelGlobal.md)| The settings information to upload. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_workspace_settings**
> put_workspace_settings(body, workspace)

Update workspace-specific settings

Updates workspace-specific settings on the server.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_settings
from gs_rest_api_settings.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_settings.DefaultApi()
body = gs_rest_api_settings.WorkspaceSettings() # WorkspaceSettings | The settings information to upload.
workspace = 'workspace_example' # str | The workspace name

try:
    # Update workspace-specific settings
    api_instance.put_workspace_settings(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->put_workspace_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WorkspaceSettings**](WorkspaceSettings.md)| The settings information to upload. | 
 **workspace** | **str**| The workspace name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# gs_rest_api_usergroup.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest/security*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_default_delete**](DefaultApi.md#group_default_delete) | **DELETE** /usergroup/groups/{group} | Delete a group
[**group_default_post**](DefaultApi.md#group_default_post) | **POST** /usergroup/groups/{group} | Add a group
[**group_delete**](DefaultApi.md#group_delete) | **DELETE** /usergroup/service/{serviceName}/groups/{group} | Delete a group
[**group_post**](DefaultApi.md#group_post) | **POST** /usergroup/service/{serviceName}/groups/{group} | Add a group
[**groups_default_get**](DefaultApi.md#groups_default_get) | **GET** /usergroup/groups/ | Query all groups
[**groups_get**](DefaultApi.md#groups_get) | **GET** /usergroup/service/{serviceName}/groups/ | Query all groups
[**user_default_delete**](DefaultApi.md#user_default_delete) | **DELETE** /usergroup/users/{user} | Delete a user
[**user_default_get**](DefaultApi.md#user_default_get) | **GET** /usergroup/users/{user} | Query a user
[**user_default_post**](DefaultApi.md#user_default_post) | **POST** /usergroup/users/{user} | Modify a user
[**user_delete**](DefaultApi.md#user_delete) | **DELETE** /usergroup/service/{serviceName}/users/{user} | Delete a user
[**user_get**](DefaultApi.md#user_get) | **GET** /usergroup/service/{serviceName}/users/{user} | Query a user
[**user_post**](DefaultApi.md#user_post) | **POST** /usergroup/service/{serviceName}/users/{user} | Modify a user
[**users_default_get**](DefaultApi.md#users_default_get) | **GET** /usergroup/users/ | Query all users
[**users_default_post**](DefaultApi.md#users_default_post) | **POST** /usergroup/users/ | Add a new user
[**users_get**](DefaultApi.md#users_get) | **GET** /usergroup/service/{serviceName}/users/ | Query all users
[**users_post**](DefaultApi.md#users_post) | **POST** /usergroup/service/{serviceName}/users/ | Add a new user

# **group_default_delete**
> group_default_delete(group)

Delete a group

Delete a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
group = 'group_example' # str | the name of the group

try:
    # Delete a group
    api_instance.group_default_delete(group)
except ApiException as e:
    print("Exception when calling DefaultApi->group_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_default_post**
> group_default_post(group)

Add a group

Add a group in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
group = 'group_example' # str | the name of the group

try:
    # Add a group
    api_instance.group_default_post(group)
except ApiException as e:
    print("Exception when calling DefaultApi->group_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete**
> group_delete(service_name, group)

Delete a group

Delete a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the user/group service
group = 'group_example' # str | the name of the group

try:
    # Delete a group
    api_instance.group_delete(service_name, group)
except ApiException as e:
    print("Exception when calling DefaultApi->group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_post**
> group_post(service_name, group)

Add a group

Add a group in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the user/group service
group = 'group_example' # str | the name of the group

try:
    # Add a group
    api_instance.group_post(service_name, group)
except ApiException as e:
    print("Exception when calling DefaultApi->group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **group** | **str**| the name of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_default_get**
> Groups groups_default_get()

Query all groups

Query all groups in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()

try:
    # Query all groups
    api_response = api_instance.groups_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> Groups groups_get(service_name)

Query all groups

Query all groups in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the group group service

try:
    # Query all groups
    api_response = api_instance.groups_get(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the group group service | 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_delete**
> user_default_delete(user)

Delete a user

Delete a user in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
user = 'user_example' # str | the name of the user

try:
    # Delete a user
    api_instance.user_default_delete(user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_default_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_get**
> User user_default_get(user)

Query a user

Query a user in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
user = 'user_example' # str | the name of the user

try:
    # Query a user
    api_response = api_instance.user_default_get(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_default_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| the name of the user | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_default_post**
> user_default_post(body, user)

Modify a user

Modify a user in the default user/group service, unspecified fields remain unchanged.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
body = gs_rest_api_usergroup.User() # User | the new user's details
user = 'user_example' # str | the name of the user

try:
    # Modify a user
    api_instance.user_default_post(body, user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| the new user&#x27;s details | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(service_name, user)

Delete a user

Delete a user in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user

try:
    # Delete a user
    api_instance.user_delete(service_name, user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get**
> User user_get(service_name, user)

Query a user

Query a user in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user

try:
    # Query a user
    api_response = api_instance.user_get(service_name, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->user_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> user_post(body, service_name, user)

Modify a user

Modify a user in a particular user/group service, unspecified fields remain unchanged.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
body = gs_rest_api_usergroup.User() # User | the new user's details
service_name = 'service_name_example' # str | the name of the user/group service
user = 'user_example' # str | the name of the user

try:
    # Modify a user
    api_instance.user_post(body, service_name, user)
except ApiException as e:
    print("Exception when calling DefaultApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| the new user&#x27;s details | 
 **service_name** | **str**| the name of the user/group service | 
 **user** | **str**| the name of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_default_get**
> Users users_default_get()

Query all users

Query all users in the default user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()

try:
    # Query all users
    api_response = api_instance.users_default_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_default_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_default_post**
> users_default_post(body)

Add a new user

Add a new user to the default user/group service

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
body = gs_rest_api_usergroup.User() # User | the new user's details

try:
    # Add a new user
    api_instance.users_default_post(body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_default_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| the new user&#x27;s details | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> Users users_get(service_name)

Query all users

Query all users in a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
service_name = 'service_name_example' # str | the name of the user/group service

try:
    # Query all users
    api_response = api_instance.users_get(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| the name of the user/group service | 

### Return type

[**Users**](Users.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(body, service_name)

Add a new user

Add a new user to a particular user/group service.

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_usergroup
from gs_rest_api_usergroup.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_usergroup.DefaultApi()
body = gs_rest_api_usergroup.User() # User | the new user's details
service_name = 'service_name_example' # str | the name of the user/group service

try:
    # Add a new user
    api_instance.users_post(body, service_name)
except ApiException as e:
    print("Exception when calling DefaultApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| the new user&#x27;s details | 
 **service_name** | **str**| the name of the user/group service | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


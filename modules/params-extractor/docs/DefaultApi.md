# gs_rest_api_params-extractor.DefaultApi

All URIs are relative to *//localhost:8080/geoserver/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_echo_parameter**](DefaultApi.md#delete_echo_parameter) | **DELETE** /params-extractor/echoes/{parameterId} | Delete an echo parameter
[**delete_rule**](DefaultApi.md#delete_rule) | **DELETE** /params-extractor/rules/{ruleId} | Delete a rule
[**get_echo_parameter**](DefaultApi.md#get_echo_parameter) | **GET** /params-extractor/echoes/{parameterId} | Retrieve a particular echo parameter definition
[**get_echo_parameters**](DefaultApi.md#get_echo_parameters) | **GET** /params-extractor/echoes | Get a list of echo parameters
[**get_rule**](DefaultApi.md#get_rule) | **GET** /params-extractor/rules/{ruleId} | Retrieve a particular rule definition
[**get_rules**](DefaultApi.md#get_rules) | **GET** /params-extractor/rules | Get a list of rules
[**post_echo_parameter**](DefaultApi.md#post_echo_parameter) | **POST** /params-extractor/echoes | Create a new echo parameter
[**post_rule**](DefaultApi.md#post_rule) | **POST** /params-extractor/rules | Create a new rule
[**put_echo_parameter**](DefaultApi.md#put_echo_parameter) | **PUT** /params-extractor/echoes/{parameterId} | Modify an echo parametr
[**put_rule**](DefaultApi.md#put_rule) | **PUT** /params-extractor/rules/{ruleId} | Modify a rule

# **delete_echo_parameter**
> delete_echo_parameter(parameter_id)

Delete an echo parameter

Deletes an echo parameter from the configuration

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
parameter_id = 'parameter_id_example' # str | The identifier of the  echo parameter to retrieve.

try:
    # Delete an echo parameter
    api_instance.delete_echo_parameter(parameter_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_echo_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The identifier of the  echo parameter to retrieve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(rule_id)

Delete a rule

Deletes a rule from the configuration

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
rule_id = 'rule_id_example' # str | The identifier of the  rule to retrieve.

try:
    # Delete a rule
    api_instance.delete_rule(rule_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The identifier of the  rule to retrieve. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_echo_parameter**
> EchoParameter get_echo_parameter(parameter_id)

Retrieve a particular echo parameter definition

Controls a particular echo parameter. Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
parameter_id = 'parameter_id_example' # str | The identifier of the  echo parameter to retrieve.

try:
    # Retrieve a particular echo parameter definition
    api_response = api_instance.get_echo_parameter(parameter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_echo_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The identifier of the  echo parameter to retrieve. | 

### Return type

[**EchoParameter**](EchoParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_echo_parameters**
> EchoParameters get_echo_parameters()

Get a list of echo parameters

List all echo parameters currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()

try:
    # Get a list of echo parameters
    api_response = api_instance.get_echo_parameters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_echo_parameters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EchoParameters**](EchoParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> Rule get_rule(rule_id)

Retrieve a particular rule definition

Controls a particular rule . Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/echos/{parameterId}.xml\" for XML).

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
rule_id = 'rule_id_example' # str | The identifier of the  rule to retrieve.

try:
    # Retrieve a particular rule definition
    api_response = api_instance.get_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The identifier of the  rule to retrieve. | 

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules**
> Rules get_rules()

Get a list of rules

List all rules currently configured.  Use the \"Accept:\" header to specify format or append an extension to the endpoint (example \"/datastores.xml\" for XML)

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()

try:
    # Get a list of rules
    api_response = api_instance.get_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Rules**](Rules.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_echo_parameter**
> str post_echo_parameter(body=body)

Create a new echo parameter

Adds a new echo parameter

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
body = gs_rest_api_params-extractor.EchoParameter() # EchoParameter |  (optional)

try:
    # Create a new echo parameter
    api_response = api_instance.post_echo_parameter(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_echo_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EchoParameter**](EchoParameter.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rule**
> str post_rule(body=body)

Create a new rule

Adds a new rule

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
body = gs_rest_api_params-extractor.Rule() # Rule |  (optional)

try:
    # Create a new rule
    api_response = api_instance.post_rule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Rule**](Rule.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_echo_parameter**
> put_echo_parameter(parameter_id, body=body)

Modify an echo parametr

Modify an echo parameter

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
parameter_id = 'parameter_id_example' # str | The identifier of the  echo parameter to retrieve.
body = gs_rest_api_params-extractor.EchoParameter() # EchoParameter |  (optional)

try:
    # Modify an echo parametr
    api_instance.put_echo_parameter(parameter_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_echo_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The identifier of the  echo parameter to retrieve. | 
 **body** | [**EchoParameter**](EchoParameter.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_rule**
> put_rule(rule_id, body=body)

Modify a rule

Modify a rule

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_params-extractor
from gs_rest_api_params-extractor.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_params-extractor.DefaultApi()
rule_id = 'rule_id_example' # str | The identifier of the  echo parameter to retrieve.
body = gs_rest_api_params-extractor.Rule() # Rule |  (optional)

try:
    # Modify a rule
    api_instance.put_rule(rule_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| The identifier of the  echo parameter to retrieve. | 
 **body** | [**Rule**](Rule.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


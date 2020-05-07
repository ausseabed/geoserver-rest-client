# gs_rest_api_gwcfilterupdate.DefaultApi

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filter_update_post**](DefaultApi.md#filter_update_post) | **POST** /filter/{filterName}/update/{updateType} | Updates a given layer filter by way of xml or zip file.

# **filter_update_post**
> filter_update_post(body, filter_name, update_type)

Updates a given layer filter by way of xml or zip file.

Restfully updates the given filterName with parameters provided in the xml or zip

### Example
```python
from __future__ import print_function
import time
import gs_rest_api_gwcfilterupdate
from gs_rest_api_gwcfilterupdate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcfilterupdate.DefaultApi()
body = gs_rest_api_gwcfilterupdate.RequestFilterUpdate() # RequestFilterUpdate | The parameters that are accepted by a given filter.
filter_name = 'filter_name_example' # str | The name of the filter to update.
update_type = 'update_type_example' # str | One of 'zip' or 'xml'

try:
    # Updates a given layer filter by way of xml or zip file.
    api_instance.filter_update_post(body, filter_name, update_type)
except ApiException as e:
    print("Exception when calling DefaultApi->filter_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestFilterUpdate**](RequestFilterUpdate.md)| The parameters that are accepted by a given filter. | 
 **filter_name** | **str**| The name of the filter to update. | 
 **update_type** | **str**| One of &#x27;zip&#x27; or &#x27;xml&#x27; | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, application/zip
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


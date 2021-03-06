# gs-rest-api-wmsstores
A WMS store is a store whose source is another WMS. Also known as \"Cascading WMS\" or \"Exernal WMS\".

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [http://geoserver.org/comm/](http://geoserver.org/comm/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/wmsstores\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/wmsstores\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_wmsstores 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_wmsstores
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_wmsstores
from gs_rest_api_wmsstores.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))
workspace = 'workspace_example' # str | Name of the workspace containing the WMS store.
store = 'store_example' # str | Name of the WMS store
recurse = true # bool | When set to true all resources contained in the store are also removed. (optional)

try:
    # Delete WMS store
    api_instance.delete_wms_store(workspace, store, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_store: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))

try:
    api_instance.delete_wms_stores()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_wms_stores: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the workspace containing the WMS store.
store = 'store_example' # str | The name of the store to be retrieved
quiet_on_not_found = true # bool | When set to true, avoids to log an Exception when the WMS store is not present. Note that 404 status code will be returned anyway. (optional)

try:
    # Retrieve a WMS store in a given workspace
    api_response = api_instance.get_wms_store(workspace, store, quiet_on_not_found=quiet_on_not_found)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_store: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))

try:
    # Get a list of WMS stores
    api_response = api_instance.get_wms_stores()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_wms_stores: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))

try:
    api_instance.post_wms_store()
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_store: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))
body = gs_rest_api_wmsstores.WMSStoreInfo() # WMSStoreInfo | WMS store body information to upload.

Examples:
- application/xml:

  ```
  <wmsStore>
    <name>remote</name>
    <capabilitiesUrl>http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities</capabilitiesUrl>
  </wmsStore>
  ```

- application/json:

  ```
  {
    "wmsStore": {
      "name": "remote",
      "capabilitiesUrl": "http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities"
    }
  }
  ```

workspace = 'workspace_example' # str | Name of the worskpace containing the WMS store.

try:
    # Add a new WMS store
    api_instance.post_wms_stores(body, workspace)
except ApiException as e:
    print("Exception when calling DefaultApi->post_wms_stores: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))
body = gs_rest_api_wmsstores.WMSStoreInfo() # WMSStoreInfo | WMS store body information to upload.
For a PUT, only values which should be changed need to be included.

Examples:
- application/xml:

  ```
  <wmsStore>
    <description>A wms store</description>
    <enabled>true</enabled>
    <__default>true</__default>
    <capabilitiesUrl>http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities</capabilitiesUrl>
    <user>admin</user>
    <password>geoserver</password>
    <maxConnections>6</maxConnections>
    <readTimeout>60</readTimeout>
    <connectTimeout>30</connectTimeout>
  </wmsStore>
  ```

- application/json:

  ```
  {
    "wmsStore": {
      "description": "A wms store",
      "enabled": "true",
      "_default": "true",
      "capabilitiesUrl": "http://demo.geoserver.org/geoserver/wms?SERVICE=WMS&VERSION=1.1.1&REQUEST=GetCapabilities",
      "user": "admin",
      "password": "geoserver",
      "maxConnections": "6",
      "readTimeout": "60",
      "connectTimeout": "30"
    }
  }
  ```

workspace = 'workspace_example' # str | The name of the worskpace containing the WMS stores.
store = 'store_example' # str | The name of the store to be retrieved

try:
    # Modify a single WMS store.
    api_instance.put_wms_store(body, workspace, store)
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_store: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_wmsstores.DefaultApi(gs_rest_api_wmsstores.ApiClient(configuration))

try:
    api_instance.put_wms_stores()
except ApiException as e:
    print("Exception when calling DefaultApi->put_wms_stores: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_wms_store**](docs/DefaultApi.md#delete_wms_store) | **DELETE** /workspaces/{workspace}/wmsstores/{store} | Delete WMS store
*DefaultApi* | [**delete_wms_stores**](docs/DefaultApi.md#delete_wms_stores) | **DELETE** /workspaces/{workspace}/wmsstores | 
*DefaultApi* | [**get_wms_store**](docs/DefaultApi.md#get_wms_store) | **GET** /workspaces/{workspace}/wmsstores/{store} | Retrieve a WMS store in a given workspace
*DefaultApi* | [**get_wms_stores**](docs/DefaultApi.md#get_wms_stores) | **GET** /workspaces/{workspace}/wmsstores | Get a list of WMS stores
*DefaultApi* | [**post_wms_store**](docs/DefaultApi.md#post_wms_store) | **POST** /workspaces/{workspace}/wmsstores/{store} | 
*DefaultApi* | [**post_wms_stores**](docs/DefaultApi.md#post_wms_stores) | **POST** /workspaces/{workspace}/wmsstores | Add a new WMS store
*DefaultApi* | [**put_wms_store**](docs/DefaultApi.md#put_wms_store) | **PUT** /workspaces/{workspace}/wmsstores/{store} | Modify a single WMS store.
*DefaultApi* | [**put_wms_stores**](docs/DefaultApi.md#put_wms_stores) | **PUT** /workspaces/{workspace}/wmsstores | 

## Documentation For Models

 - [WMSStoreInfo](docs/WMSStoreInfo.md)
 - [WMSStoresList](docs/WMSStoresList.md)
 - [WMSStoresListItem](docs/WMSStoresListItem.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

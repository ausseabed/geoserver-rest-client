# gs-rest-api-structuredcoverages
A structured coverage store allows description of its \"granules\" and management of them.

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/structuredcoverages\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/structuredcoverages\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_structuredcoverages 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_structuredcoverages
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_structuredcoverages
from gs_rest_api_structuredcoverages.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.delete_coverage_stores()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_coverage_stores: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
granule_id = 'granule_id_example' # str | The granule ID
purge = 'purge_example' # str | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\" and \"all\". When set to \"none\" data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \"metadata\" delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
update_b_box = gs_rest_api_structuredcoverages.Object() # Object | When set to \"true\", triggers re-calculation of the layer native bbox. Defaults to \"false\". (optional)

try:
    api_instance.delete_structured_coverage_granule(workspace, store, coverage, granule_id, purge=purge, update_b_box=update_b_box)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_structured_coverage_granule: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
filter = 'filter_example' # str | A CQL filter to reduce the returned granules (optional)
purge = 'purge_example' # str | The purge parameter specifies if and how the underlying raster data source is deleted. Allowable values for this parameter are \"none\", \"metadata\" and \"all\". When set to \"none\" data and auxiliary files are preserved, only the registration in the mosaic is removed When set to \"metadata\" delete only auxiliary files and metadata (e.g. NetCDF sidecar indexes). It’s recommended when data files (such as granules) should not be deleted from disk. Finally, when set to \"all\" both data and auxiliary files are removed. (optional)
update_b_box = gs_rest_api_structuredcoverages.Object() # Object | When set to \"true\", triggers re-calculation of the layer native bbox. Defaults to \"false\". (optional)

try:
    api_instance.delete_structured_coverage_granules(workspace, store, coverage, filter=filter, purge=purge, update_b_box=update_b_box)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_structured_coverage_granules: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
granule_id = 'granule_id_example' # str | The granule ID

try:
    # Get the attributes of a particular granule
    api_instance.get_structured_coverage_granule(workspace, store, coverage, granule_id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_structured_coverage_granule: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved
filter = 'filter_example' # str | A CQL filter to reduce the returned granules (optional)
offset = 56 # int | Used for paging, the start of the current page (optional)
limit = 56 # int | Used for paging, the number of items to be returned (optional)

try:
    # Get the attributes associated to the granules
    api_instance.get_structured_coverage_granules(workspace, store, coverage, filter=filter, offset=offset, limit=limit)
except ApiException as e:
    print("Exception when calling DefaultApi->get_structured_coverage_granules: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))
workspace = 'workspace_example' # str | The name of the worskpace containing the coverage stores.
store = 'store_example' # str | The name of the store to be retrieved
coverage = 'coverage_example' # str | The name of the coverage to be retrieved

try:
    # Get the information schema attached to the granules
    api_response = api_instance.get_structured_coverage_index(workspace, store, coverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_structured_coverage_index: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.post_structured_coverage_granule()
except ApiException as e:
    print("Exception when calling DefaultApi->post_structured_coverage_granule: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.post_structured_coverage_granules()
except ApiException as e:
    print("Exception when calling DefaultApi->post_structured_coverage_granules: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.post_structured_coverage_index()
except ApiException as e:
    print("Exception when calling DefaultApi->post_structured_coverage_index: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.put_structured_coverage_granule()
except ApiException as e:
    print("Exception when calling DefaultApi->put_structured_coverage_granule: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.put_structured_coverage_granules()
except ApiException as e:
    print("Exception when calling DefaultApi->put_structured_coverage_granules: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_structuredcoverages.DefaultApi(gs_rest_api_structuredcoverages.ApiClient(configuration))

try:
    api_instance.put_structured_coverage_index()
except ApiException as e:
    print("Exception when calling DefaultApi->put_structured_coverage_index: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_coverage_stores**](docs/DefaultApi.md#delete_coverage_stores) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
*DefaultApi* | [**delete_structured_coverage_granule**](docs/DefaultApi.md#delete_structured_coverage_granule) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*DefaultApi* | [**delete_structured_coverage_granules**](docs/DefaultApi.md#delete_structured_coverage_granules) | **DELETE** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*DefaultApi* | [**get_structured_coverage_granule**](docs/DefaultApi.md#get_structured_coverage_granule) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | Get the attributes of a particular granule
*DefaultApi* | [**get_structured_coverage_granules**](docs/DefaultApi.md#get_structured_coverage_granules) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | Get the attributes associated to the granules
*DefaultApi* | [**get_structured_coverage_index**](docs/DefaultApi.md#get_structured_coverage_index) | **GET** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | Get the information schema attached to the granules
*DefaultApi* | [**post_structured_coverage_granule**](docs/DefaultApi.md#post_structured_coverage_granule) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*DefaultApi* | [**post_structured_coverage_granules**](docs/DefaultApi.md#post_structured_coverage_granules) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*DefaultApi* | [**post_structured_coverage_index**](docs/DefaultApi.md#post_structured_coverage_index) | **POST** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 
*DefaultApi* | [**put_structured_coverage_granule**](docs/DefaultApi.md#put_structured_coverage_granule) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules/{granuleId} | 
*DefaultApi* | [**put_structured_coverage_granules**](docs/DefaultApi.md#put_structured_coverage_granules) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index/granules | 
*DefaultApi* | [**put_structured_coverage_index**](docs/DefaultApi.md#put_structured_coverage_index) | **PUT** /workspaces/{workspace}/coveragestores/{store}/coverages/{coverage}/index | 

## Documentation For Models

 - [Attribute](docs/Attribute.md)
 - [Schema](docs/Schema.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
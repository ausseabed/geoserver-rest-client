# gs-rest-api-gwcmasstruncate
The REST API for mass truncation provides a mechanism for completely clearing caches more conveniently than with the seeding system

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/gwcmasstruncate\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/gwcmasstruncate\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_gwcmasstruncate 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_gwcmasstruncate
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_gwcmasstruncate
from gs_rest_api_gwcmasstruncate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcmasstruncate.DefaultApi(gs_rest_api_gwcmasstruncate.ApiClient(configuration))

try:
    # Returns available request types for truncation
    api_instance.masstruncate_get()
except ApiException as e:
    print("Exception when calling DefaultApi->masstruncate_get: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_gwcmasstruncate.DefaultApi(gs_rest_api_gwcmasstruncate.ApiClient(configuration))
request_type = 'request_type_example' # str | The requestType parameter is used to control which cached tiles to truncate.
layer = 'layer_example' # str | The layername to truncate (optional)

try:
    # Issue a mass truncate request
    api_instance.masstruncate_post(request_type, layer=layer)
except ApiException as e:
    print("Exception when calling DefaultApi->masstruncate_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**masstruncate_get**](docs/DefaultApi.md#masstruncate_get) | **GET** /masstruncate | Returns available request types for truncation
*DefaultApi* | [**masstruncate_post**](docs/DefaultApi.md#masstruncate_post) | **POST** /masstruncate | Issue a mass truncate request

## Documentation For Models


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

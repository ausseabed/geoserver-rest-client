# gs-rest-api-gwcfilterupdate
The REST API for Updating GWC filter

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/gwcfilterupdate\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/gwcfilterupdate\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_gwcfilterupdate 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_gwcfilterupdate
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_gwcfilterupdate
from gs_rest_api_gwcfilterupdate.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_gwcfilterupdate.DefaultApi(gs_rest_api_gwcfilterupdate.ApiClient(configuration))
body = gs_rest_api_gwcfilterupdate.RequestFilterUpdate() # RequestFilterUpdate | The parameters that are accepted by a given filter.
filter_name = 'filter_name_example' # str | The name of the filter to update.
update_type = 'update_type_example' # str | One of 'zip' or 'xml'

try:
    # Updates a given layer filter by way of xml or zip file.
    api_instance.filter_update_post(body, filter_name, update_type)
except ApiException as e:
    print("Exception when calling DefaultApi->filter_update_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080/geoserver/gwc/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**filter_update_post**](docs/DefaultApi.md#filter_update_post) | **POST** /filter/{filterName}/update/{updateType} | Updates a given layer filter by way of xml or zip file.

## Documentation For Models

 - [RequestFilterUpdate](docs/RequestFilterUpdate.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
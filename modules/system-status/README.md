# gs-rest-api-system-status
Request provides details about OWS and REST requests that GeoServer has handled

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/system-status\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/system-status\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_system-status 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_system-status
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_system-status
from gs_rest_api_system-status.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_system-status.DefaultApi(gs_rest_api_system-status.ApiClient(configuration))

try:
    # Get a list of requests
    api_response = api_instance.get_monitor_requests()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_monitor_requests: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_monitor_requests**](docs/DefaultApi.md#get_monitor_requests) | **GET** /about/system-status | Get a list of requests

## Documentation For Models

 - [Metrics](docs/Metrics.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

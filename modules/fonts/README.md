# gs-rest-api-fonts
A font is a set of characters that can be used in a style for displaying labels.

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/fonts\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/fonts\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_fonts 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_fonts
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_fonts
from gs_rest_api_fonts.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_fonts.DefaultApi(gs_rest_api_fonts.ApiClient(configuration))

try:
    api_instance.delete_fonts()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_fonts: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_fonts.DefaultApi(gs_rest_api_fonts.ApiClient(configuration))

try:
    # Get a list of fonts
    api_response = api_instance.get_fonts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_fonts: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_fonts.DefaultApi(gs_rest_api_fonts.ApiClient(configuration))

try:
    api_instance.post_fonts()
except ApiException as e:
    print("Exception when calling DefaultApi->post_fonts: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_fonts.DefaultApi(gs_rest_api_fonts.ApiClient(configuration))

try:
    api_instance.put_fonts()
except ApiException as e:
    print("Exception when calling DefaultApi->put_fonts: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_fonts**](docs/DefaultApi.md#delete_fonts) | **DELETE** /fonts | 
*DefaultApi* | [**get_fonts**](docs/DefaultApi.md#get_fonts) | **GET** /fonts | Get a list of fonts
*DefaultApi* | [**post_fonts**](docs/DefaultApi.md#post_fonts) | **POST** /fonts | 
*DefaultApi* | [**put_fonts**](docs/DefaultApi.md#put_fonts) | **PUT** /fonts | 

## Documentation For Models

 - [FontList](docs/FontList.md)
 - [FontListItem](docs/FontListItem.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net
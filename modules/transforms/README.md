# gs-rest-api-transforms
A transform contains a style sheet that can be used to generate a new textual output format of user choosing for WFS

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/transforms\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/transforms\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_transforms 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_transforms
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_transforms
from gs_rest_api_transforms.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))
transform = 'transform_example' # str | Name of the transformation.

try:
    # Delete transformation
    api_instance.delete_tranform(transform)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_tranform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))

try:
    api_instance.delete_transform()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_transform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))
transform = 'transform_example' # str | Name of the transformation.

try:
    # Retrieve a transformation.
    api_response = api_instance.get_transform(transform)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))

try:
    # List available transformations.
    api_response = api_instance.get_transforms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_transforms: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))

try:
    api_instance.post_tranform()
except ApiException as e:
    print("Exception when calling DefaultApi->post_tranform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))
body = gs_rest_api_transforms.Transform() # Transform | Transform body to upload.
name = 'name_example' # str | Name of the transformation. (optional)
source_format = 'source_format_example' # str | Source format of the transformation. (optional)
output_format = 'output_format_example' # str | Output format of the transformation. (optional)
output_mime_type = 'output_mime_type_example' # str | Output mime type of the transformation. (optional)
file_extension = 'file_extension_example' # str | The extension of the file generated by the transformation. (optional)

try:
    # Add a new transform
    api_instance.post_transform(body, name=name, source_format=source_format, output_format=output_format, output_mime_type=output_mime_type, file_extension=file_extension)
except ApiException as e:
    print("Exception when calling DefaultApi->post_transform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))
body = gs_rest_api_transforms.Transform() # Transform | Transform body to upload.
transform = 'transform_example' # str | Name of the transformation.

try:
    # Modify a single transform
    api_instance.put_tranform(body, transform)
except ApiException as e:
    print("Exception when calling DefaultApi->put_tranform: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_transforms.DefaultApi(gs_rest_api_transforms.ApiClient(configuration))

try:
    api_instance.put_transform()
except ApiException as e:
    print("Exception when calling DefaultApi->put_transform: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**delete_tranform**](docs/DefaultApi.md#delete_tranform) | **DELETE** /services/wfs/transforms/{transform} | Delete transformation
*DefaultApi* | [**delete_transform**](docs/DefaultApi.md#delete_transform) | **DELETE** /services/wfs/transforms | 
*DefaultApi* | [**get_transform**](docs/DefaultApi.md#get_transform) | **GET** /services/wfs/transforms/{transform} | Retrieve a transformation.
*DefaultApi* | [**get_transforms**](docs/DefaultApi.md#get_transforms) | **GET** /services/wfs/transforms | List available transformations.
*DefaultApi* | [**post_tranform**](docs/DefaultApi.md#post_tranform) | **POST** /services/wfs/transforms/{transform} | 
*DefaultApi* | [**post_transform**](docs/DefaultApi.md#post_transform) | **POST** /services/wfs/transforms | Add a new transform
*DefaultApi* | [**put_tranform**](docs/DefaultApi.md#put_tranform) | **PUT** /services/wfs/transforms/{transform} | Modify a single transform
*DefaultApi* | [**put_transform**](docs/DefaultApi.md#put_transform) | **PUT** /services/wfs/transforms | 

## Documentation For Models

 - [Transform](docs/Transform.md)
 - [TransformList](docs/TransformList.md)
 - [TransformListItem](docs/TransformListItem.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

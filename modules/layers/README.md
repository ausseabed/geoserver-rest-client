# gs-rest-api-layers
A layer is a published resource (feature type or coverage).

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
pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/layers\&ignore=.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ausseabed/geoserver-rest-client.git#subdirectory=modules/layers\&ignore=.git`)

Then import the package:
```python
import gs_rest_api_layers 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gs_rest_api_layers
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import gs_rest_api_layers
from gs_rest_api_layers.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_delete: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    # Get a list of layers
    api_response = api_instance.layers_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_get: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
layer_name = 'layer_name_example' # str | The name of the layer to delete.
recurse = true # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional)

try:
    # Delete layer
    api_instance.layers_name_delete(layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_delete: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
layer_name = 'layer_name_example' # str | The name of the layer to retrieve.

try:
    # Retrieve a layer
    api_response = api_instance.layers_name_get(layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_get: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_name_post()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_post: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
body = gs_rest_api_layers.LayerWrapper() # LayerWrapper | The updated layer definition.
layer_name = 'layer_name_example' # str | The name of the layer to modify.

try:
    # Modify a layer.
    api_instance.layers_name_put(body, layer_name)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_put: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
workspace_name = gs_rest_api_layers.Object() # Object | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to delete.
recurse = true # bool | Recursively removes the layer from all layer groups which reference it. If this results in an empty layer group, also delete the layer group. Allowed values for this parameter are true or false. The default value is false. A request with 'recurse=false' will fail if any layer groups reference the layer. (optional)

try:
    # Delete layer
    api_instance.layers_name_workspace_delete(workspace_name, layer_name, recurse=recurse)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_workspace_delete: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to retrieve.

try:
    # Retrieve a layer
    api_response = api_instance.layers_name_workspace_get(workspace_name, layer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_workspace_get: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_name_workspace_post()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_workspace_post: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
body = gs_rest_api_layers.LayerWrapper() # LayerWrapper | The updated layer definition.
workspace_name = gs_rest_api_layers.Object() # Object | The name of the workspace the layer is in.
layer_name = 'layer_name_example' # str | The name of the layer to modify.

try:
    # Modify a layer.
    api_instance.layers_name_workspace_put(body, workspace_name, layer_name)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_name_workspace_put: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_post()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_post: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_put()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_put: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_workspace_delete()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_workspace_delete: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))
workspace_name = 'workspace_name_example' # str | The name of the workspace to list layers in

try:
    # Get a list of layers in a workspace.
    api_response = api_instance.layers_workspace_get(workspace_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->layers_workspace_get: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_workspace_post()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_workspace_post: %s\n" % e)

# create an instance of the API class
api_instance = gs_rest_api_layers.DefaultApi(gs_rest_api_layers.ApiClient(configuration))

try:
    api_instance.layers_workspace_put()
except ApiException as e:
    print("Exception when calling DefaultApi->layers_workspace_put: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *//localhost:8080/geoserver/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**layers_delete**](docs/DefaultApi.md#layers_delete) | **DELETE** /layers | 
*DefaultApi* | [**layers_get**](docs/DefaultApi.md#layers_get) | **GET** /layers | Get a list of layers
*DefaultApi* | [**layers_name_delete**](docs/DefaultApi.md#layers_name_delete) | **DELETE** /layers/{layerName} | Delete layer
*DefaultApi* | [**layers_name_get**](docs/DefaultApi.md#layers_name_get) | **GET** /layers/{layerName} | Retrieve a layer
*DefaultApi* | [**layers_name_post**](docs/DefaultApi.md#layers_name_post) | **POST** /layers/{layerName} | 
*DefaultApi* | [**layers_name_put**](docs/DefaultApi.md#layers_name_put) | **PUT** /layers/{layerName} | Modify a layer.
*DefaultApi* | [**layers_name_workspace_delete**](docs/DefaultApi.md#layers_name_workspace_delete) | **DELETE** /workspaces/{workspaceName}/layers/{layerName} | Delete layer
*DefaultApi* | [**layers_name_workspace_get**](docs/DefaultApi.md#layers_name_workspace_get) | **GET** /workspaces/{workspaceName}/layers/{layerName} | Retrieve a layer
*DefaultApi* | [**layers_name_workspace_post**](docs/DefaultApi.md#layers_name_workspace_post) | **POST** /workspaces/{workspaceName}/layers/{layerName} | 
*DefaultApi* | [**layers_name_workspace_put**](docs/DefaultApi.md#layers_name_workspace_put) | **PUT** /workspaces/{workspaceName}/layers/{layerName} | Modify a layer.
*DefaultApi* | [**layers_post**](docs/DefaultApi.md#layers_post) | **POST** /layers | 
*DefaultApi* | [**layers_put**](docs/DefaultApi.md#layers_put) | **PUT** /layers | 
*DefaultApi* | [**layers_workspace_delete**](docs/DefaultApi.md#layers_workspace_delete) | **DELETE** /workspaces/{workspaceName}/layers | 
*DefaultApi* | [**layers_workspace_get**](docs/DefaultApi.md#layers_workspace_get) | **GET** /workspaces/{workspaceName}/layers | Get a list of layers in a workspace.
*DefaultApi* | [**layers_workspace_post**](docs/DefaultApi.md#layers_workspace_post) | **POST** /workspaces/{workspaceName}/layers | 
*DefaultApi* | [**layers_workspace_put**](docs/DefaultApi.md#layers_workspace_put) | **PUT** /workspaces/{workspaceName}/layers | 

## Documentation For Models

 - [Layer](docs/Layer.md)
 - [LayerReference](docs/LayerReference.md)
 - [LayerWrapper](docs/LayerWrapper.md)
 - [Layers](docs/Layers.md)
 - [MetadataEntry](docs/MetadataEntry.md)
 - [StyleReference](docs/StyleReference.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

geoserver-users@sourceforge.net

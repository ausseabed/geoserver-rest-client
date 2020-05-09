# coding: utf-8

# flake8: noqa

"""
    GeoServer Data Stores

    A data store contains vector format spatial data. It can be a file (such as a shapefile), a database (such as PostGIS), or a server (such as a remote Web Feature Service).  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from gs_rest_api_datastores.api.default_api import DefaultApi

# import ApiClient
from gs_rest_api_datastores.api_client import ApiClient
from gs_rest_api_datastores.configuration import Configuration
from gs_rest_api_datastores.exceptions import OpenApiException
from gs_rest_api_datastores.exceptions import ApiTypeError
from gs_rest_api_datastores.exceptions import ApiValueError
from gs_rest_api_datastores.exceptions import ApiKeyError
from gs_rest_api_datastores.exceptions import ApiException
# import models into sdk package
from gs_rest_api_datastores.model.datastore import Datastore
from gs_rest_api_datastores.model.entry import Entry
from gs_rest_api_datastores.model.workspace import Workspace


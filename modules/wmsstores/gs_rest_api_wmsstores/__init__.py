# coding: utf-8

# flake8: noqa

"""
    GeoServer WMS Stores

    A WMS store is a store whose source is another WMS. Also known as \"Cascading WMS\" or \"Exernal WMS\".  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from gs_rest_api_wmsstores.api.default_api import DefaultApi
# import ApiClient
from gs_rest_api_wmsstores.api_client import ApiClient
from gs_rest_api_wmsstores.configuration import Configuration
# import models into sdk package
from gs_rest_api_wmsstores.model.wms_store_info import WMSStoreInfo
from gs_rest_api_wmsstores.model.wms_stores_list import WMSStoresList
from gs_rest_api_wmsstores.model.wms_stores_list_item import WMSStoresListItem
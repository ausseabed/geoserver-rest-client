# coding: utf-8

# flake8: noqa
"""
    GeoServer Feature Types

    A feature type is a vector based spatial resource or data set that originates from a data store. In some cases, such as with a shapefile, a feature type has a one-to-one relationship with its data store. In other cases, such as PostGIS, the relationship of feature type to data store is many-to-one, feature types corresponding to a table in the database.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from gs_rest_api_featuretypes.model.feature_type_info import FeatureTypeInfo
from gs_rest_api_featuretypes.model.metadata_entry import MetadataEntry
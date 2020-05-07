# coding: utf-8

"""
    GeoServer WMS Store Layers

    A WMS store is a store whose source is another WMS. Also known as \"Cascading WMS\" or \"External WMS\". A WMS store layer is a layer from this store.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gs-rest-api-wmslayers"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="GeoServer WMS Store Layers",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoServer WMS Store Layers"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A WMS store is a store whose source is another WMS. Also known as \&quot;Cascading WMS\&quot; or \&quot;External WMS\&quot;. A WMS store layer is a layer from this store.  # noqa: E501
    """
)

# coding: utf-8

"""
    GeoWebCache Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gs-rest-api-gwclayers"
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
    description="GeoWebCache Layers",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoWebCache Layers"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A layer is a published resource (feature type or coverage).  # noqa: E501
    """
)

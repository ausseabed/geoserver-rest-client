# coding: utf-8

"""
    GeoServer XSLT transforms

    A transform contains a style sheet that can be used to generate a new textual output format of user choosing for WFS  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gs-rest-api-transforms"
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
    description="GeoServer XSLT transforms",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoServer XSLT transforms"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A transform contains a style sheet that can be used to generate a new textual output format of user choosing for WFS  # noqa: E501
    """
)

# coding: utf-8

"""
    GeoWebCache Memory Cache Statistics

    A response contains memory cache statistics  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gs-rest-api-gwcmemorycachestatistics"
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
    description="GeoWebCache Memory Cache Statistics",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoWebCache Memory Cache Statistics"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A response contains memory cache statistics  # noqa: E501
    """
)

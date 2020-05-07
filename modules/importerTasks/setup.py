# coding: utf-8

"""
    GeoServer Importer Extension - Tasks

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The tasks endpoint controls individual tasks within an import job. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "gs-rest-api-importerTasks"
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
    description="GeoServer Importer Extension - Tasks",
    author_email="geoserver-users@sourceforge.net",
    url="",
    keywords=["Swagger", "GeoServer Importer Extension - Tasks"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The tasks endpoint controls individual tasks within an import job. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501
    """
)

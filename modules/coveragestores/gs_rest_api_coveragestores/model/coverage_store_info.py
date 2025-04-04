# coding: utf-8

"""
    GeoServer CoverageStores

    A coverage store describes how access a raster data source.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CoverageStoreInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'enabled': 'bool',
        'workspace': 'object',
        'default__': 'bool',
        'url': 'str',
        'coverages': 'object',
        'metadata': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'enabled': 'enabled',
        'workspace': 'workspace',
        'default__': '__default__',
        'url': 'url',
        'coverages': 'coverages',
        'metadata': 'metadata'
    }

    def __init__(self, name=None, description=None, type=None, enabled=None, workspace=None, default__=None, url=None, coverages=None, metadata=None):  # noqa: E501
        """CoverageStoreInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._type = None
        self._enabled = None
        self._workspace = None
        self._default__ = None
        self._url = None
        self._coverages = None
        self._metadata = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if enabled is not None:
            self.enabled = enabled
        if workspace is not None:
            self.workspace = workspace
        if default__ is not None:
            self.default__ = default__
        if url is not None:
            self.url = url
        if coverages is not None:
            self.coverages = coverages
        if metadata is not None:
            self.metadata = metadata

    @property
    def name(self):
        """Gets the name of this CoverageStoreInfo.  # noqa: E501

        Name of the coverage store  # noqa: E501

        :return: The name of this CoverageStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CoverageStoreInfo.

        Name of the coverage store  # noqa: E501

        :param name: The name of this CoverageStoreInfo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CoverageStoreInfo.  # noqa: E501

        Description of the coverage store  # noqa: E501

        :return: The description of this CoverageStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CoverageStoreInfo.

        Description of the coverage store  # noqa: E501

        :param description: The description of this CoverageStoreInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this CoverageStoreInfo.  # noqa: E501

        Type of coverage store  # noqa: E501

        :return: The type of this CoverageStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoverageStoreInfo.

        Type of coverage store  # noqa: E501

        :param type: The type of this CoverageStoreInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this CoverageStoreInfo.  # noqa: E501

        Whether the store is enabled, or not  # noqa: E501

        :return: The enabled of this CoverageStoreInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CoverageStoreInfo.

        Whether the store is enabled, or not  # noqa: E501

        :param enabled: The enabled of this CoverageStoreInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def workspace(self):
        """Gets the workspace of this CoverageStoreInfo.  # noqa: E501

        The workspace containing the store  # noqa: E501

        :return: The workspace of this CoverageStoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CoverageStoreInfo.

        The workspace containing the store  # noqa: E501

        :param workspace: The workspace of this CoverageStoreInfo.  # noqa: E501
        :type: object
        """

        self._workspace = workspace

    @property
    def default__(self):
        """Gets the default__ of this CoverageStoreInfo.  # noqa: E501

        Whether the store is the default store of the workspace  # noqa: E501

        :return: The default__ of this CoverageStoreInfo.  # noqa: E501
        :rtype: bool
        """
        return self._default__

    @default__.setter
    def default__(self, default__):
        """Sets the default__ of this CoverageStoreInfo.

        Whether the store is the default store of the workspace  # noqa: E501

        :param default__: The default__ of this CoverageStoreInfo.  # noqa: E501
        :type: bool
        """

        self._default__ = default__

    @property
    def url(self):
        """Gets the url of this CoverageStoreInfo.  # noqa: E501

        Location of the raster data source (often, but not necessarily, a file). Can be relative to the data directory.  # noqa: E501

        :return: The url of this CoverageStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CoverageStoreInfo.

        Location of the raster data source (often, but not necessarily, a file). Can be relative to the data directory.  # noqa: E501

        :param url: The url of this CoverageStoreInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def coverages(self):
        """Gets the coverages of this CoverageStoreInfo.  # noqa: E501


        :return: The coverages of this CoverageStoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._coverages

    @coverages.setter
    def coverages(self, coverages):
        """Sets the coverages of this CoverageStoreInfo.


        :param coverages: The coverages of this CoverageStoreInfo.  # noqa: E501
        :type: object
        """

        self._coverages = coverages

    @property
    def metadata(self):
        """Gets the metadata of this CoverageStoreInfo.  # noqa: E501

        Metadata for the coverage store  # noqa: E501

        :return: The metadata of this CoverageStoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this CoverageStoreInfo.

        Metadata for the coverage store  # noqa: E501

        :param metadata: The metadata of this CoverageStoreInfo.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CoverageStoreInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CoverageStoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

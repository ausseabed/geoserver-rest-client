# coding: utf-8

"""
    GeoServer Namespace

    A namespace is a uniquely identifiable grouping of feature types. It is identified by a prefix and a URI.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class NamespaceResponse(object):
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
        'prefix': 'str',
        'uri': 'str',
        'feature_types': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'uri': 'uri',
        'feature_types': 'featureTypes'
    }

    def __init__(self, prefix=None, uri=None, feature_types=None):  # noqa: E501
        """NamespaceResponse - a model defined in Swagger"""  # noqa: E501
        self._prefix = None
        self._uri = None
        self._feature_types = None
        self.discriminator = None
        if prefix is not None:
            self.prefix = prefix
        if uri is not None:
            self.uri = uri
        if feature_types is not None:
            self.feature_types = feature_types

    @property
    def prefix(self):
        """Gets the prefix of this NamespaceResponse.  # noqa: E501

        Name of namespace  # noqa: E501

        :return: The prefix of this NamespaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this NamespaceResponse.

        Name of namespace  # noqa: E501

        :param prefix: The prefix of this NamespaceResponse.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def uri(self):
        """Gets the uri of this NamespaceResponse.  # noqa: E501

        URI of the namespace  # noqa: E501

        :return: The uri of this NamespaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this NamespaceResponse.

        URI of the namespace  # noqa: E501

        :param uri: The uri of this NamespaceResponse.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def feature_types(self):
        """Gets the feature_types of this NamespaceResponse.  # noqa: E501

        URL to featureTypes associated with this namespace  # noqa: E501

        :return: The feature_types of this NamespaceResponse.  # noqa: E501
        :rtype: str
        """
        return self._feature_types

    @feature_types.setter
    def feature_types(self, feature_types):
        """Sets the feature_types of this NamespaceResponse.

        URL to featureTypes associated with this namespace  # noqa: E501

        :param feature_types: The feature_types of this NamespaceResponse.  # noqa: E501
        :type: str
        """

        self._feature_types = feature_types

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
        if issubclass(NamespaceResponse, dict):
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
        if not isinstance(other, NamespaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

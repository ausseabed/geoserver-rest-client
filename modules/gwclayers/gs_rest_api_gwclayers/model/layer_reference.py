# coding: utf-8

"""
    GeoWebCache Layers

    A layer is a published resource (feature type or coverage).  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LayerReference(object):
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
        'link': 'str'
    }

    attribute_map = {
        'name': 'name',
        'link': 'link'
    }

    def __init__(self, name=None, link=None):  # noqa: E501
        """LayerReference - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._link = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if link is not None:
            self.link = link

    @property
    def name(self):
        """Gets the name of this LayerReference.  # noqa: E501

        Name of layer  # noqa: E501

        :return: The name of this LayerReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LayerReference.

        Name of layer  # noqa: E501

        :param name: The name of this LayerReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def link(self):
        """Gets the link of this LayerReference.  # noqa: E501

        URL to layer definition  # noqa: E501

        :return: The link of this LayerReference.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this LayerReference.

        URL to layer definition  # noqa: E501

        :param link: The link of this LayerReference.  # noqa: E501
        :type: str
        """

        self._link = link

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
        if issubclass(LayerReference, dict):
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
        if not isinstance(other, LayerReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

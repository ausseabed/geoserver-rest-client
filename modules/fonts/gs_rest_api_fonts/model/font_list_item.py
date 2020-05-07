# coding: utf-8

"""
    GeoServer Fonts

    A font is a set of characters that can be used in a style for displaying labels.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class FontListItem(object):
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
        'entry': 'str'
    }

    attribute_map = {
        'entry': 'entry'
    }

    def __init__(self, entry=None):  # noqa: E501
        """FontListItem - a model defined in Swagger"""  # noqa: E501
        self._entry = None
        self.discriminator = None
        if entry is not None:
            self.entry = entry

    @property
    def entry(self):
        """Gets the entry of this FontListItem.  # noqa: E501

        Name of font  # noqa: E501

        :return: The entry of this FontListItem.  # noqa: E501
        :rtype: str
        """
        return self._entry

    @entry.setter
    def entry(self, entry):
        """Sets the entry of this FontListItem.

        Name of font  # noqa: E501

        :param entry: The entry of this FontListItem.  # noqa: E501
        :type: str
        """

        self._entry = entry

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
        if issubclass(FontListItem, dict):
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
        if not isinstance(other, FontListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    GeoServer StructuredCoverageStores

    A structured coverage store allows description of its \"granules\" and management of them.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Attribute(object):
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
        'min_occurs': 'int',
        'max_occurs': 'int',
        'nillable': 'bool',
        'binding': 'str',
        'length': 'int'
    }

    attribute_map = {
        'name': 'name',
        'min_occurs': 'minOccurs',
        'max_occurs': 'maxOccurs',
        'nillable': 'nillable',
        'binding': 'binding',
        'length': 'length'
    }

    def __init__(self, name=None, min_occurs=None, max_occurs=None, nillable=None, binding=None, length=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._min_occurs = None
        self._max_occurs = None
        self._nillable = None
        self._binding = None
        self._length = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if min_occurs is not None:
            self.min_occurs = min_occurs
        if max_occurs is not None:
            self.max_occurs = max_occurs
        if nillable is not None:
            self.nillable = nillable
        if binding is not None:
            self.binding = binding
        if length is not None:
            self.length = length

    @property
    def name(self):
        """Gets the name of this Attribute.  # noqa: E501

        Name of the attribute  # noqa: E501

        :return: The name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attribute.

        Name of the attribute  # noqa: E501

        :param name: The name of this Attribute.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def min_occurs(self):
        """Gets the min_occurs of this Attribute.  # noqa: E501

        Minimum number of occurences (0 for optional attribute)  # noqa: E501

        :return: The min_occurs of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._min_occurs

    @min_occurs.setter
    def min_occurs(self, min_occurs):
        """Sets the min_occurs of this Attribute.

        Minimum number of occurences (0 for optional attribute)  # noqa: E501

        :param min_occurs: The min_occurs of this Attribute.  # noqa: E501
        :type: int
        """

        self._min_occurs = min_occurs

    @property
    def max_occurs(self):
        """Gets the max_occurs of this Attribute.  # noqa: E501

        Maximumn number of occurences (normally 1)  # noqa: E501

        :return: The max_occurs of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._max_occurs

    @max_occurs.setter
    def max_occurs(self, max_occurs):
        """Sets the max_occurs of this Attribute.

        Maximumn number of occurences (normally 1)  # noqa: E501

        :param max_occurs: The max_occurs of this Attribute.  # noqa: E501
        :type: int
        """

        self._max_occurs = max_occurs

    @property
    def nillable(self):
        """Gets the nillable of this Attribute.  # noqa: E501

        If the attribute can be missing  # noqa: E501

        :return: The nillable of this Attribute.  # noqa: E501
        :rtype: bool
        """
        return self._nillable

    @nillable.setter
    def nillable(self, nillable):
        """Sets the nillable of this Attribute.

        If the attribute can be missing  # noqa: E501

        :param nillable: The nillable of this Attribute.  # noqa: E501
        :type: bool
        """

        self._nillable = nillable

    @property
    def binding(self):
        """Gets the binding of this Attribute.  # noqa: E501

        Name of the java class for the attribute  # noqa: E501

        :return: The binding of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._binding

    @binding.setter
    def binding(self, binding):
        """Sets the binding of this Attribute.

        Name of the java class for the attribute  # noqa: E501

        :param binding: The binding of this Attribute.  # noqa: E501
        :type: str
        """

        self._binding = binding

    @property
    def length(self):
        """Gets the length of this Attribute.  # noqa: E501

        Length of the field  # noqa: E501

        :return: The length of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this Attribute.

        Length of the field  # noqa: E501

        :param length: The length of this Attribute.  # noqa: E501
        :type: int
        """

        self._length = length

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    GeoServer XSLT transforms

    A transform contains a style sheet that can be used to generate a new textual output format of user choosing for WFS  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Transform(object):
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
        'source_format': 'str',
        'output_format': 'str',
        'xslt': 'str'
    }

    attribute_map = {
        'name': 'name',
        'source_format': 'sourceFormat',
        'output_format': 'outputFormat',
        'xslt': 'xslt'
    }

    def __init__(self, name=None, source_format=None, output_format=None, xslt=None):  # noqa: E501
        """Transform - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._source_format = None
        self._output_format = None
        self._xslt = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if source_format is not None:
            self.source_format = source_format
        if output_format is not None:
            self.output_format = output_format
        if xslt is not None:
            self.xslt = xslt

    @property
    def name(self):
        """Gets the name of this Transform.  # noqa: E501

        Name of the transformation  # noqa: E501

        :return: The name of this Transform.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Transform.

        Name of the transformation  # noqa: E501

        :param name: The name of this Transform.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def source_format(self):
        """Gets the source_format of this Transform.  # noqa: E501

        Source format accepted by the transformation  # noqa: E501

        :return: The source_format of this Transform.  # noqa: E501
        :rtype: str
        """
        return self._source_format

    @source_format.setter
    def source_format(self, source_format):
        """Sets the source_format of this Transform.

        Source format accepted by the transformation  # noqa: E501

        :param source_format: The source_format of this Transform.  # noqa: E501
        :type: str
        """

        self._source_format = source_format

    @property
    def output_format(self):
        """Gets the output_format of this Transform.  # noqa: E501

        Output format produced by the transformation  # noqa: E501

        :return: The output_format of this Transform.  # noqa: E501
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        """Sets the output_format of this Transform.

        Output format produced by the transformation  # noqa: E501

        :param output_format: The output_format of this Transform.  # noqa: E501
        :type: str
        """

        self._output_format = output_format

    @property
    def xslt(self):
        """Gets the xslt of this Transform.  # noqa: E501

        Style sheet associated with the transformation  # noqa: E501

        :return: The xslt of this Transform.  # noqa: E501
        :rtype: str
        """
        return self._xslt

    @xslt.setter
    def xslt(self, xslt):
        """Sets the xslt of this Transform.

        Style sheet associated with the transformation  # noqa: E501

        :param xslt: The xslt of this Transform.  # noqa: E501
        :type: str
        """

        self._xslt = xslt

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
        if issubclass(Transform, dict):
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
        if not isinstance(other, Transform):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

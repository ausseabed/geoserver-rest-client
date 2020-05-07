# coding: utf-8

"""
    GeoServer Template

    Manage templates used to configure output (for example GetFeatureInfo reponse). Templates can be registered for the entire server or workspace. You can also configure a template for use with a store, featureType or coverage.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Templates(object):
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
        'layer_groups': 'object'
    }

    attribute_map = {
        'layer_groups': 'layerGroups'
    }

    def __init__(self, layer_groups=None):  # noqa: E501
        """Templates - a model defined in Swagger"""  # noqa: E501
        self._layer_groups = None
        self.discriminator = None
        if layer_groups is not None:
            self.layer_groups = layer_groups

    @property
    def layer_groups(self):
        """Gets the layer_groups of this Templates.  # noqa: E501


        :return: The layer_groups of this Templates.  # noqa: E501
        :rtype: object
        """
        return self._layer_groups

    @layer_groups.setter
    def layer_groups(self, layer_groups):
        """Sets the layer_groups of this Templates.


        :param layer_groups: The layer_groups of this Templates.  # noqa: E501
        :type: object
        """

        self._layer_groups = layer_groups

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
        if issubclass(Templates, dict):
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
        if not isinstance(other, Templates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    GeoServer System Status

    Request provides details about OWS and REST requests that GeoServer has handled  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Metrics(object):
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
        'metric': 'object'
    }

    attribute_map = {
        'metric': 'metric'
    }

    def __init__(self, metric=None):  # noqa: E501
        """Metrics - a model defined in Swagger"""  # noqa: E501
        self._metric = None
        self.discriminator = None
        if metric is not None:
            self.metric = metric

    @property
    def metric(self):
        """Gets the metric of this Metrics.  # noqa: E501

        Metrics for system status properties  # noqa: E501

        :return: The metric of this Metrics.  # noqa: E501
        :rtype: object
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Metrics.

        Metrics for system status properties  # noqa: E501

        :param metric: The metric of this Metrics.  # noqa: E501
        :type: object
        """

        self._metric = metric

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
        if issubclass(Metrics, dict):
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
        if not isinstance(other, Metrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

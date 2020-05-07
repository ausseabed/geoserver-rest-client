# coding: utf-8

"""
    GeoServer Importer Extension - Main

    The Importer extension gives a GeoServer administrator an alternate, more-streamlined method for uploading and configuring new layers. The main endpoint manages individual import jobs. The importer extension is an optional install and may not be available on all deployments of GeoServer  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Bbox(object):
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
        'minx': 'str',
        'miny': 'str',
        'maxx': 'str',
        'maxy': 'str',
        'crs': 'str'
    }

    attribute_map = {
        'minx': 'minx',
        'miny': 'miny',
        'maxx': 'maxx',
        'maxy': 'maxy',
        'crs': 'crs'
    }

    def __init__(self, minx=None, miny=None, maxx=None, maxy=None, crs=None):  # noqa: E501
        """Bbox - a model defined in Swagger"""  # noqa: E501
        self._minx = None
        self._miny = None
        self._maxx = None
        self._maxy = None
        self._crs = None
        self.discriminator = None
        if minx is not None:
            self.minx = minx
        if miny is not None:
            self.miny = miny
        if maxx is not None:
            self.maxx = maxx
        if maxy is not None:
            self.maxy = maxy
        if crs is not None:
            self.crs = crs

    @property
    def minx(self):
        """Gets the minx of this Bbox.  # noqa: E501

        The minimum x value  # noqa: E501

        :return: The minx of this Bbox.  # noqa: E501
        :rtype: str
        """
        return self._minx

    @minx.setter
    def minx(self, minx):
        """Sets the minx of this Bbox.

        The minimum x value  # noqa: E501

        :param minx: The minx of this Bbox.  # noqa: E501
        :type: str
        """

        self._minx = minx

    @property
    def miny(self):
        """Gets the miny of this Bbox.  # noqa: E501

        The minimum y value  # noqa: E501

        :return: The miny of this Bbox.  # noqa: E501
        :rtype: str
        """
        return self._miny

    @miny.setter
    def miny(self, miny):
        """Sets the miny of this Bbox.

        The minimum y value  # noqa: E501

        :param miny: The miny of this Bbox.  # noqa: E501
        :type: str
        """

        self._miny = miny

    @property
    def maxx(self):
        """Gets the maxx of this Bbox.  # noqa: E501

        The maximum x value  # noqa: E501

        :return: The maxx of this Bbox.  # noqa: E501
        :rtype: str
        """
        return self._maxx

    @maxx.setter
    def maxx(self, maxx):
        """Sets the maxx of this Bbox.

        The maximum x value  # noqa: E501

        :param maxx: The maxx of this Bbox.  # noqa: E501
        :type: str
        """

        self._maxx = maxx

    @property
    def maxy(self):
        """Gets the maxy of this Bbox.  # noqa: E501

        The maximum y value  # noqa: E501

        :return: The maxy of this Bbox.  # noqa: E501
        :rtype: str
        """
        return self._maxy

    @maxy.setter
    def maxy(self, maxy):
        """Sets the maxy of this Bbox.

        The maximum y value  # noqa: E501

        :param maxy: The maxy of this Bbox.  # noqa: E501
        :type: str
        """

        self._maxy = maxy

    @property
    def crs(self):
        """Gets the crs of this Bbox.  # noqa: E501

        The WKT representation of the CRS.  # noqa: E501

        :return: The crs of this Bbox.  # noqa: E501
        :rtype: str
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """Sets the crs of this Bbox.

        The WKT representation of the CRS.  # noqa: E501

        :param crs: The crs of this Bbox.  # noqa: E501
        :type: str
        """

        self._crs = crs

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
        if issubclass(Bbox, dict):
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
        if not isinstance(other, Bbox):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

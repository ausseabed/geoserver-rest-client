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


class Layer(object):
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
        'href': 'str',
        'title': 'str',
        'abstract': 'str',
        'description': 'str',
        'original_name': 'str',
        'native_name': 'str',
        'srs': 'str',
        'bbox': 'Bbox',
        'attributes': 'FeatureType',
        'style': 'Style'
    }

    attribute_map = {
        'name': 'name',
        'href': 'href',
        'title': 'title',
        'abstract': 'abstract',
        'description': 'description',
        'original_name': 'originalName',
        'native_name': 'nativeName',
        'srs': 'srs',
        'bbox': 'bbox',
        'attributes': 'attributes',
        'style': 'style'
    }

    def __init__(self, name=None, href=None, title=None, abstract=None, description=None, original_name=None, native_name=None, srs=None, bbox=None, attributes=None, style=None):  # noqa: E501
        """Layer - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._href = None
        self._title = None
        self._abstract = None
        self._description = None
        self._original_name = None
        self._native_name = None
        self._srs = None
        self._bbox = None
        self._attributes = None
        self._style = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if href is not None:
            self.href = href
        if title is not None:
            self.title = title
        if abstract is not None:
            self.abstract = abstract
        if description is not None:
            self.description = description
        if original_name is not None:
            self.original_name = original_name
        if native_name is not None:
            self.native_name = native_name
        if srs is not None:
            self.srs = srs
        if bbox is not None:
            self.bbox = bbox
        if attributes is not None:
            self.attributes = attributes
        if style is not None:
            self.style = style

    @property
    def name(self):
        """Gets the name of this Layer.  # noqa: E501

        The name of the layer  # noqa: E501

        :return: The name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Layer.

        The name of the layer  # noqa: E501

        :param name: The name of this Layer.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def href(self):
        """Gets the href of this Layer.  # noqa: E501

        URL to the importer layer endpoint  # noqa: E501

        :return: The href of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Layer.

        URL to the importer layer endpoint  # noqa: E501

        :param href: The href of this Layer.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def title(self):
        """Gets the title of this Layer.  # noqa: E501

        The layer title  # noqa: E501

        :return: The title of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Layer.

        The layer title  # noqa: E501

        :param title: The title of this Layer.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def abstract(self):
        """Gets the abstract of this Layer.  # noqa: E501

        The layer abstract  # noqa: E501

        :return: The abstract of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """Sets the abstract of this Layer.

        The layer abstract  # noqa: E501

        :param abstract: The abstract of this Layer.  # noqa: E501
        :type: str
        """

        self._abstract = abstract

    @property
    def description(self):
        """Gets the description of this Layer.  # noqa: E501

        The layer description  # noqa: E501

        :return: The description of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Layer.

        The layer description  # noqa: E501

        :param description: The description of this Layer.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def original_name(self):
        """Gets the original_name of this Layer.  # noqa: E501

        The original name of the layer. This may be different from the name if this name already exists in geoserver.  # noqa: E501

        :return: The original_name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this Layer.

        The original name of the layer. This may be different from the name if this name already exists in geoserver.  # noqa: E501

        :param original_name: The original_name of this Layer.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

    @property
    def native_name(self):
        """Gets the native_name of this Layer.  # noqa: E501

        The name of the underlying resource  # noqa: E501

        :return: The native_name of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._native_name

    @native_name.setter
    def native_name(self, native_name):
        """Sets the native_name of this Layer.

        The name of the underlying resource  # noqa: E501

        :param native_name: The native_name of this Layer.  # noqa: E501
        :type: str
        """

        self._native_name = native_name

    @property
    def srs(self):
        """Gets the srs of this Layer.  # noqa: E501

        The SRS of the layer  # noqa: E501

        :return: The srs of this Layer.  # noqa: E501
        :rtype: str
        """
        return self._srs

    @srs.setter
    def srs(self, srs):
        """Sets the srs of this Layer.

        The SRS of the layer  # noqa: E501

        :param srs: The srs of this Layer.  # noqa: E501
        :type: str
        """

        self._srs = srs

    @property
    def bbox(self):
        """Gets the bbox of this Layer.  # noqa: E501


        :return: The bbox of this Layer.  # noqa: E501
        :rtype: Bbox
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this Layer.


        :param bbox: The bbox of this Layer.  # noqa: E501
        :type: Bbox
        """

        self._bbox = bbox

    @property
    def attributes(self):
        """Gets the attributes of this Layer.  # noqa: E501


        :return: The attributes of this Layer.  # noqa: E501
        :rtype: FeatureType
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Layer.


        :param attributes: The attributes of this Layer.  # noqa: E501
        :type: FeatureType
        """

        self._attributes = attributes

    @property
    def style(self):
        """Gets the style of this Layer.  # noqa: E501


        :return: The style of this Layer.  # noqa: E501
        :rtype: Style
        """
        return self._style

    @style.setter
    def style(self, style):
        """Sets the style of this Layer.


        :param style: The style of this Layer.  # noqa: E501
        :type: Style
        """

        self._style = style

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
        if issubclass(Layer, dict):
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
        if not isinstance(other, Layer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
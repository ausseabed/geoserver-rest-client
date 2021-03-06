# coding: utf-8

"""
    GeoServer Resources

    A resource is any item in the data directory that does not represent configuration. Typical resources include styles and icons.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ResourceDirectory(object):
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
        'parent': 'object',
        'last_modified': 'str',
        'type': 'str',
        'children': 'object'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'name': 'name',
        'parent': 'parent',
        'last_modified': 'lastModified',
        'type': 'type',
        'children': 'children'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, name=None, parent=None, last_modified=None, type=None, children=None, *args, **kwargs):  # noqa: E501
        """ResourceDirectory - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._parent = None
        self._last_modified = None
        self._type = None
        self._children = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if parent is not None:
            self.parent = parent
        if last_modified is not None:
            self.last_modified = last_modified
        if type is not None:
            self.type = type
        if children is not None:
            self.children = children
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this ResourceDirectory.  # noqa: E501

        The name of the resource, including the extension if applicable.  # noqa: E501

        :return: The name of this ResourceDirectory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResourceDirectory.

        The name of the resource, including the extension if applicable.  # noqa: E501

        :param name: The name of this ResourceDirectory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this ResourceDirectory.  # noqa: E501

        The parent resource of this one  # noqa: E501

        :return: The parent of this ResourceDirectory.  # noqa: E501
        :rtype: object
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this ResourceDirectory.

        The parent resource of this one  # noqa: E501

        :param parent: The parent of this ResourceDirectory.  # noqa: E501
        :type: object
        """

        self._parent = parent

    @property
    def last_modified(self):
        """Gets the last_modified of this ResourceDirectory.  # noqa: E501

        The last modified date of the resource  # noqa: E501

        :return: The last_modified of this ResourceDirectory.  # noqa: E501
        :rtype: str
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this ResourceDirectory.

        The last modified date of the resource  # noqa: E501

        :param last_modified: The last_modified of this ResourceDirectory.  # noqa: E501
        :type: str
        """

        self._last_modified = last_modified

    @property
    def type(self):
        """Gets the type of this ResourceDirectory.  # noqa: E501

        Type of resource.  # noqa: E501

        :return: The type of this ResourceDirectory.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceDirectory.

        Type of resource.  # noqa: E501

        :param type: The type of this ResourceDirectory.  # noqa: E501
        :type: str
        """
        allowed_values = ["resource", "directory"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def children(self):
        """Gets the children of this ResourceDirectory.  # noqa: E501

        List of child resources in the directory  # noqa: E501

        :return: The children of this ResourceDirectory.  # noqa: E501
        :rtype: object
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this ResourceDirectory.

        List of child resources in the directory  # noqa: E501

        :param children: The children of this ResourceDirectory.  # noqa: E501
        :type: object
        """

        self._children = children

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
        if issubclass(ResourceDirectory, dict):
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
        if not isinstance(other, ResourceDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

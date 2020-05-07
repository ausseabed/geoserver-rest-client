# coding: utf-8

"""
    GeoServer WMTS Stores

    A WMTS store is a store whose source is a remote WMTS. Also known as \"Cascading WMTS\".  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: geoserver-users@sourceforge.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class WMTSStoreInfo(object):
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
        'description': 'str',
        'type': 'str',
        'enabled': 'bool',
        'workspace': 'object',
        'metadata': 'object',
        'default__': 'bool',
        'capabilities_url': 'str',
        'user': 'str',
        'password': 'str',
        'max_connections': 'float',
        'read_timeout': 'str',
        'connect_timeout': 'str',
        'wmts_layers': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'enabled': 'enabled',
        'workspace': 'workspace',
        'metadata': 'metadata',
        'default__': '__default__',
        'capabilities_url': 'capabilitiesURL',
        'user': 'user',
        'password': 'password',
        'max_connections': 'maxConnections',
        'read_timeout': 'readTimeout',
        'connect_timeout': 'connectTimeout',
        'wmts_layers': 'wmtsLayers'
    }

    def __init__(self, name=None, description=None, type=None, enabled=None, workspace=None, metadata=None, default__=None, capabilities_url=None, user=None, password=None, max_connections=None, read_timeout=None, connect_timeout=None, wmts_layers=None):  # noqa: E501
        """WMTSStoreInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._type = None
        self._enabled = None
        self._workspace = None
        self._metadata = None
        self._default__ = None
        self._capabilities_url = None
        self._user = None
        self._password = None
        self._max_connections = None
        self._read_timeout = None
        self._connect_timeout = None
        self._wmts_layers = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if workspace is not None:
            self.workspace = workspace
        if metadata is not None:
            self.metadata = metadata
        if default__ is not None:
            self.default__ = default__
        if capabilities_url is not None:
            self.capabilities_url = capabilities_url
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if max_connections is not None:
            self.max_connections = max_connections
        if read_timeout is not None:
            self.read_timeout = read_timeout
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if wmts_layers is not None:
            self.wmts_layers = wmts_layers

    @property
    def name(self):
        """Gets the name of this WMTSStoreInfo.  # noqa: E501

        Name of the WMTS store  # noqa: E501

        :return: The name of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WMTSStoreInfo.

        Name of the WMTS store  # noqa: E501

        :param name: The name of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WMTSStoreInfo.  # noqa: E501

        Description of the WMTS store  # noqa: E501

        :return: The description of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WMTSStoreInfo.

        Description of the WMTS store  # noqa: E501

        :param description: The description of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this WMTSStoreInfo.  # noqa: E501

        Type of store. Set to WMTS.  # noqa: E501

        :return: The type of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WMTSStoreInfo.

        Type of store. Set to WMTS.  # noqa: E501

        :param type: The type of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this WMTSStoreInfo.  # noqa: E501

        Whether the store is enabled  # noqa: E501

        :return: The enabled of this WMTSStoreInfo.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this WMTSStoreInfo.

        Whether the store is enabled  # noqa: E501

        :param enabled: The enabled of this WMTSStoreInfo.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def workspace(self):
        """Gets the workspace of this WMTSStoreInfo.  # noqa: E501

        Workspace containing the store  # noqa: E501

        :return: The workspace of this WMTSStoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this WMTSStoreInfo.

        Workspace containing the store  # noqa: E501

        :param workspace: The workspace of this WMTSStoreInfo.  # noqa: E501
        :type: object
        """

        self._workspace = workspace

    @property
    def metadata(self):
        """Gets the metadata of this WMTSStoreInfo.  # noqa: E501

        Miscellaneous configuration details about the WMTS store  # noqa: E501

        :return: The metadata of this WMTSStoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WMTSStoreInfo.

        Miscellaneous configuration details about the WMTS store  # noqa: E501

        :param metadata: The metadata of this WMTSStoreInfo.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def default__(self):
        """Gets the default__ of this WMTSStoreInfo.  # noqa: E501

        Whether the store is the default store of the workspace  # noqa: E501

        :return: The default__ of this WMTSStoreInfo.  # noqa: E501
        :rtype: bool
        """
        return self._default__

    @default__.setter
    def default__(self, default__):
        """Sets the default__ of this WMTSStoreInfo.

        Whether the store is the default store of the workspace  # noqa: E501

        :param default__: The default__ of this WMTSStoreInfo.  # noqa: E501
        :type: bool
        """

        self._default__ = default__

    @property
    def capabilities_url(self):
        """Gets the capabilities_url of this WMTSStoreInfo.  # noqa: E501

        Location of the WMTS capabilities URL where the store originates  # noqa: E501

        :return: The capabilities_url of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._capabilities_url

    @capabilities_url.setter
    def capabilities_url(self, capabilities_url):
        """Sets the capabilities_url of this WMTSStoreInfo.

        Location of the WMTS capabilities URL where the store originates  # noqa: E501

        :param capabilities_url: The capabilities_url of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._capabilities_url = capabilities_url

    @property
    def user(self):
        """Gets the user of this WMTSStoreInfo.  # noqa: E501

        User name to use when connecting to the remote WMTS  # noqa: E501

        :return: The user of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this WMTSStoreInfo.

        User name to use when connecting to the remote WMTS  # noqa: E501

        :param user: The user of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def password(self):
        """Gets the password of this WMTSStoreInfo.  # noqa: E501

        Password or hash to use when connecting to the remote WMTS  # noqa: E501

        :return: The password of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this WMTSStoreInfo.

        Password or hash to use when connecting to the remote WMTS  # noqa: E501

        :param password: The password of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def max_connections(self):
        """Gets the max_connections of this WMTSStoreInfo.  # noqa: E501

        Maximum number of simultaneous connections to use  # noqa: E501

        :return: The max_connections of this WMTSStoreInfo.  # noqa: E501
        :rtype: float
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        """Sets the max_connections of this WMTSStoreInfo.

        Maximum number of simultaneous connections to use  # noqa: E501

        :param max_connections: The max_connections of this WMTSStoreInfo.  # noqa: E501
        :type: float
        """

        self._max_connections = max_connections

    @property
    def read_timeout(self):
        """Gets the read_timeout of this WMTSStoreInfo.  # noqa: E501

        Time in seconds before read time out  # noqa: E501

        :return: The read_timeout of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this WMTSStoreInfo.

        Time in seconds before read time out  # noqa: E501

        :param read_timeout: The read_timeout of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._read_timeout = read_timeout

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this WMTSStoreInfo.  # noqa: E501

        Time in seconds before connection time out  # noqa: E501

        :return: The connect_timeout of this WMTSStoreInfo.  # noqa: E501
        :rtype: str
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this WMTSStoreInfo.

        Time in seconds before connection time out  # noqa: E501

        :param connect_timeout: The connect_timeout of this WMTSStoreInfo.  # noqa: E501
        :type: str
        """

        self._connect_timeout = connect_timeout

    @property
    def wmts_layers(self):
        """Gets the wmts_layers of this WMTSStoreInfo.  # noqa: E501


        :return: The wmts_layers of this WMTSStoreInfo.  # noqa: E501
        :rtype: list[object]
        """
        return self._wmts_layers

    @wmts_layers.setter
    def wmts_layers(self, wmts_layers):
        """Sets the wmts_layers of this WMTSStoreInfo.


        :param wmts_layers: The wmts_layers of this WMTSStoreInfo.  # noqa: E501
        :type: list[object]
        """

        self._wmts_layers = wmts_layers

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
        if issubclass(WMTSStoreInfo, dict):
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
        if not isinstance(other, WMTSStoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

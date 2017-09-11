# coding: utf-8

"""
    

     # Basic sequence  - Register a sensor system - `POST /ss` - Add one or more data streams to the sensor system - `POST /ss/{sysid}` - Add data stream observations - `POST /ss/{sysid}/{strid}/obs`        

    OpenAPI spec version: 0.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Geometry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'dimension': 'int',
        'boundary': 'Geometry',
        'state_flag': 'int',
        'description': 'VertexDescription',
        'empty': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'dimension': 'dimension',
        'boundary': 'boundary',
        'state_flag': 'stateFlag',
        'description': 'description',
        'empty': 'empty',
        'type': 'type'
    }

    def __init__(self, dimension=None, boundary=None, state_flag=None, description=None, empty=None, type=None):
        """
        Geometry - a model defined in Swagger
        """

        self._dimension = None
        self._boundary = None
        self._state_flag = None
        self._description = None
        self._empty = None
        self._type = None

        self.dimension = dimension
        self.boundary = boundary
        self.state_flag = state_flag
        self.description = description
        self.empty = empty
        self.type = type

    @property
    def dimension(self):
        """
        Gets the dimension of this Geometry.

        :return: The dimension of this Geometry.
        :rtype: int
        """
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        """
        Sets the dimension of this Geometry.

        :param dimension: The dimension of this Geometry.
        :type: int
        """
        if dimension is None:
            raise ValueError("Invalid value for `dimension`, must not be `None`")

        self._dimension = dimension

    @property
    def boundary(self):
        """
        Gets the boundary of this Geometry.

        :return: The boundary of this Geometry.
        :rtype: Geometry
        """
        return self._boundary

    @boundary.setter
    def boundary(self, boundary):
        """
        Sets the boundary of this Geometry.

        :param boundary: The boundary of this Geometry.
        :type: Geometry
        """
        if boundary is None:
            raise ValueError("Invalid value for `boundary`, must not be `None`")

        self._boundary = boundary

    @property
    def state_flag(self):
        """
        Gets the state_flag of this Geometry.

        :return: The state_flag of this Geometry.
        :rtype: int
        """
        return self._state_flag

    @state_flag.setter
    def state_flag(self, state_flag):
        """
        Sets the state_flag of this Geometry.

        :param state_flag: The state_flag of this Geometry.
        :type: int
        """
        if state_flag is None:
            raise ValueError("Invalid value for `state_flag`, must not be `None`")

        self._state_flag = state_flag

    @property
    def description(self):
        """
        Gets the description of this Geometry.

        :return: The description of this Geometry.
        :rtype: VertexDescription
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Geometry.

        :param description: The description of this Geometry.
        :type: VertexDescription
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def empty(self):
        """
        Gets the empty of this Geometry.

        :return: The empty of this Geometry.
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """
        Sets the empty of this Geometry.

        :param empty: The empty of this Geometry.
        :type: bool
        """
        if empty is None:
            raise ValueError("Invalid value for `empty`, must not be `None`")

        self._empty = empty

    @property
    def type(self):
        """
        Gets the type of this Geometry.

        :return: The type of this Geometry.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Geometry.

        :param type: The type of this Geometry.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")
        allowed_values = ["Unknown", "Point", "Line", "Envelope", "MultiPoint", "Polyline", "Polygon"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Geometry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

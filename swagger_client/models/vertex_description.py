# coding: utf-8

"""
    

     # Basic sequence  - Register a sensor system - `POST /ss` - Add one or more data streams to the sensor system - `POST /ss/{sysid}` - Add data stream observations - `POST /ss/{sysid}/{strid}/obs`        

    OpenAPI spec version: 0.3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VertexDescription(object):
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
        'total_component_count': 'int',
        'attribute_count': 'int'
    }

    attribute_map = {
        'total_component_count': 'totalComponentCount',
        'attribute_count': 'attributeCount'
    }

    def __init__(self, total_component_count=None, attribute_count=None):
        """
        VertexDescription - a model defined in Swagger
        """

        self._total_component_count = None
        self._attribute_count = None

        self.total_component_count = total_component_count
        self.attribute_count = attribute_count

    @property
    def total_component_count(self):
        """
        Gets the total_component_count of this VertexDescription.

        :return: The total_component_count of this VertexDescription.
        :rtype: int
        """
        return self._total_component_count

    @total_component_count.setter
    def total_component_count(self, total_component_count):
        """
        Sets the total_component_count of this VertexDescription.

        :param total_component_count: The total_component_count of this VertexDescription.
        :type: int
        """
        if total_component_count is None:
            raise ValueError("Invalid value for `total_component_count`, must not be `None`")

        self._total_component_count = total_component_count

    @property
    def attribute_count(self):
        """
        Gets the attribute_count of this VertexDescription.

        :return: The attribute_count of this VertexDescription.
        :rtype: int
        """
        return self._attribute_count

    @attribute_count.setter
    def attribute_count(self, attribute_count):
        """
        Sets the attribute_count of this VertexDescription.

        :param attribute_count: The attribute_count of this VertexDescription.
        :type: int
        """
        if attribute_count is None:
            raise ValueError("Invalid value for `attribute_count`, must not be `None`")

        self._attribute_count = attribute_count

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
        if not isinstance(other, VertexDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

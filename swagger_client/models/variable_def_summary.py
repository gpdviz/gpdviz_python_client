# coding: utf-8

"""
    Gpdviz REST API

    The Gpdviz REST API deals with three main kinds of resources: sensor systems, data streams, and observations.

    OpenAPI spec version: 0.4.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VariableDefSummary(object):
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
        'sysid': 'str',
        'strid': 'str',
        'name': 'str',
        'units': 'str'
    }

    attribute_map = {
        'sysid': 'sysid',
        'strid': 'strid',
        'name': 'name',
        'units': 'units'
    }

    def __init__(self, sysid=None, strid=None, name=None, units=None):
        """
        VariableDefSummary - a model defined in Swagger
        """

        self._sysid = None
        self._strid = None
        self._name = None
        self._units = None

        self.sysid = sysid
        self.strid = strid
        self.name = name
        if units is not None:
          self.units = units

    @property
    def sysid(self):
        """
        Gets the sysid of this VariableDefSummary.

        :return: The sysid of this VariableDefSummary.
        :rtype: str
        """
        return self._sysid

    @sysid.setter
    def sysid(self, sysid):
        """
        Sets the sysid of this VariableDefSummary.

        :param sysid: The sysid of this VariableDefSummary.
        :type: str
        """
        if sysid is None:
            raise ValueError("Invalid value for `sysid`, must not be `None`")

        self._sysid = sysid

    @property
    def strid(self):
        """
        Gets the strid of this VariableDefSummary.

        :return: The strid of this VariableDefSummary.
        :rtype: str
        """
        return self._strid

    @strid.setter
    def strid(self, strid):
        """
        Sets the strid of this VariableDefSummary.

        :param strid: The strid of this VariableDefSummary.
        :type: str
        """
        if strid is None:
            raise ValueError("Invalid value for `strid`, must not be `None`")

        self._strid = strid

    @property
    def name(self):
        """
        Gets the name of this VariableDefSummary.

        :return: The name of this VariableDefSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VariableDefSummary.

        :param name: The name of this VariableDefSummary.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def units(self):
        """
        Gets the units of this VariableDefSummary.

        :return: The units of this VariableDefSummary.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this VariableDefSummary.

        :param units: The units of this VariableDefSummary.
        :type: str
        """

        self._units = units

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
        if not isinstance(other, VariableDefSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class ObservationsAdd(object):
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
        'observations': 'dict(str, list[ObsData])'
    }

    attribute_map = {
        'observations': 'observations'
    }

    def __init__(self, observations=None):
        """
        ObservationsAdd - a model defined in Swagger
        """

        self._observations = None

        self.observations = observations

    @property
    def observations(self):
        """
        Gets the observations of this ObservationsAdd.

        :return: The observations of this ObservationsAdd.
        :rtype: dict(str, list[ObsData])
        """
        return self._observations

    @observations.setter
    def observations(self, observations):
        """
        Sets the observations of this ObservationsAdd.

        :param observations: The observations of this ObservationsAdd.
        :type: dict(str, list[ObsData])
        """
        if observations is None:
            raise ValueError("Invalid value for `observations`, must not be `None`")

        self._observations = observations

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
        if not isinstance(other, ObservationsAdd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

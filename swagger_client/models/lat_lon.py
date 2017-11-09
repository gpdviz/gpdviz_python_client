# coding: utf-8

"""
    Gpdviz REST API

    The Gpdviz REST API deals with three main kinds of resources: sensor systems, data streams, and observations.

    OpenAPI spec version: 0.4.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LatLon(object):
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
        'lat': 'float',
        'lon': 'float'
    }

    attribute_map = {
        'lat': 'lat',
        'lon': 'lon'
    }

    def __init__(self, lat=None, lon=None):
        """
        LatLon - a model defined in Swagger
        """

        self._lat = None
        self._lon = None

        self.lat = lat
        self.lon = lon

    @property
    def lat(self):
        """
        Gets the lat of this LatLon.

        :return: The lat of this LatLon.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """
        Sets the lat of this LatLon.

        :param lat: The lat of this LatLon.
        :type: float
        """
        if lat is None:
            raise ValueError("Invalid value for `lat`, must not be `None`")

        self._lat = lat

    @property
    def lon(self):
        """
        Gets the lon of this LatLon.

        :return: The lon of this LatLon.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """
        Sets the lon of this LatLon.

        :param lon: The lon of this LatLon.
        :type: float
        """
        if lon is None:
            raise ValueError("Invalid value for `lon`, must not be `None`")

        self._lon = lon

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
        if not isinstance(other, LatLon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

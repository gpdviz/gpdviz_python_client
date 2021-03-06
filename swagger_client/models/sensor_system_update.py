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


class SensorSystemUpdate(object):
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
        'push_events': 'float',
        'center': 'LatLon',
        'zoom': 'float'
    }

    attribute_map = {
        'push_events': 'pushEvents',
        'center': 'center',
        'zoom': 'zoom'
    }

    def __init__(self, push_events=None, center=None, zoom=None):
        """
        SensorSystemUpdate - a model defined in Swagger
        """

        self._push_events = None
        self._center = None
        self._zoom = None

        if push_events is not None:
          self.push_events = push_events
        if center is not None:
          self.center = center
        if zoom is not None:
          self.zoom = zoom

    @property
    def push_events(self):
        """
        Gets the push_events of this SensorSystemUpdate.

        :return: The push_events of this SensorSystemUpdate.
        :rtype: float
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        """
        Sets the push_events of this SensorSystemUpdate.

        :param push_events: The push_events of this SensorSystemUpdate.
        :type: float
        """

        self._push_events = push_events

    @property
    def center(self):
        """
        Gets the center of this SensorSystemUpdate.

        :return: The center of this SensorSystemUpdate.
        :rtype: LatLon
        """
        return self._center

    @center.setter
    def center(self, center):
        """
        Sets the center of this SensorSystemUpdate.

        :param center: The center of this SensorSystemUpdate.
        :type: LatLon
        """

        self._center = center

    @property
    def zoom(self):
        """
        Gets the zoom of this SensorSystemUpdate.

        :return: The zoom of this SensorSystemUpdate.
        :rtype: float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom of this SensorSystemUpdate.

        :param zoom: The zoom of this SensorSystemUpdate.
        :type: float
        """

        self._zoom = zoom

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
        if not isinstance(other, SensorSystemUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

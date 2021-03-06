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


class SensorSystem(object):
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
        'name': 'str',
        'description': 'str',
        'push_events': 'bool',
        'center': 'LatLon',
        'zoom': 'float',
        'click_listener': 'str',
        'streams': 'dict(str, DataStream)'
    }

    attribute_map = {
        'sysid': 'sysid',
        'name': 'name',
        'description': 'description',
        'push_events': 'pushEvents',
        'center': 'center',
        'zoom': 'zoom',
        'click_listener': 'clickListener',
        'streams': 'streams'
    }

    def __init__(self, sysid=None, name=None, description=None, push_events=None, center=None, zoom=None, click_listener=None, streams=None):
        """
        SensorSystem - a model defined in Swagger
        """

        self._sysid = None
        self._name = None
        self._description = None
        self._push_events = None
        self._center = None
        self._zoom = None
        self._click_listener = None
        self._streams = None

        self.sysid = sysid
        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        self.push_events = push_events
        if center is not None:
          self.center = center
        if zoom is not None:
          self.zoom = zoom
        if click_listener is not None:
          self.click_listener = click_listener
        self.streams = streams

    @property
    def sysid(self):
        """
        Gets the sysid of this SensorSystem.

        :return: The sysid of this SensorSystem.
        :rtype: str
        """
        return self._sysid

    @sysid.setter
    def sysid(self, sysid):
        """
        Sets the sysid of this SensorSystem.

        :param sysid: The sysid of this SensorSystem.
        :type: str
        """
        if sysid is None:
            raise ValueError("Invalid value for `sysid`, must not be `None`")

        self._sysid = sysid

    @property
    def name(self):
        """
        Gets the name of this SensorSystem.

        :return: The name of this SensorSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SensorSystem.

        :param name: The name of this SensorSystem.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this SensorSystem.

        :return: The description of this SensorSystem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SensorSystem.

        :param description: The description of this SensorSystem.
        :type: str
        """

        self._description = description

    @property
    def push_events(self):
        """
        Gets the push_events of this SensorSystem.

        :return: The push_events of this SensorSystem.
        :rtype: bool
        """
        return self._push_events

    @push_events.setter
    def push_events(self, push_events):
        """
        Sets the push_events of this SensorSystem.

        :param push_events: The push_events of this SensorSystem.
        :type: bool
        """
        if push_events is None:
            raise ValueError("Invalid value for `push_events`, must not be `None`")

        self._push_events = push_events

    @property
    def center(self):
        """
        Gets the center of this SensorSystem.

        :return: The center of this SensorSystem.
        :rtype: LatLon
        """
        return self._center

    @center.setter
    def center(self, center):
        """
        Sets the center of this SensorSystem.

        :param center: The center of this SensorSystem.
        :type: LatLon
        """

        self._center = center

    @property
    def zoom(self):
        """
        Gets the zoom of this SensorSystem.

        :return: The zoom of this SensorSystem.
        :rtype: float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """
        Sets the zoom of this SensorSystem.

        :param zoom: The zoom of this SensorSystem.
        :type: float
        """

        self._zoom = zoom

    @property
    def click_listener(self):
        """
        Gets the click_listener of this SensorSystem.

        :return: The click_listener of this SensorSystem.
        :rtype: str
        """
        return self._click_listener

    @click_listener.setter
    def click_listener(self, click_listener):
        """
        Sets the click_listener of this SensorSystem.

        :param click_listener: The click_listener of this SensorSystem.
        :type: str
        """

        self._click_listener = click_listener

    @property
    def streams(self):
        """
        Gets the streams of this SensorSystem.

        :return: The streams of this SensorSystem.
        :rtype: dict(str, DataStream)
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """
        Sets the streams of this SensorSystem.

        :param streams: The streams of this SensorSystem.
        :type: dict(str, DataStream)
        """
        if streams is None:
            raise ValueError("Invalid value for `streams`, must not be `None`")

        self._streams = streams

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
        if not isinstance(other, SensorSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

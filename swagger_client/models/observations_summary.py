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


class ObservationsSummary(object):
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
        'time': 'str',
        'added': 'float',
        'removed': 'float'
    }

    attribute_map = {
        'sysid': 'sysid',
        'strid': 'strid',
        'time': 'time',
        'added': 'added',
        'removed': 'removed'
    }

    def __init__(self, sysid=None, strid=None, time=None, added=None, removed=None):
        """
        ObservationsSummary - a model defined in Swagger
        """

        self._sysid = None
        self._strid = None
        self._time = None
        self._added = None
        self._removed = None

        self.sysid = sysid
        self.strid = strid
        if time is not None:
          self.time = time
        if added is not None:
          self.added = added
        if removed is not None:
          self.removed = removed

    @property
    def sysid(self):
        """
        Gets the sysid of this ObservationsSummary.

        :return: The sysid of this ObservationsSummary.
        :rtype: str
        """
        return self._sysid

    @sysid.setter
    def sysid(self, sysid):
        """
        Sets the sysid of this ObservationsSummary.

        :param sysid: The sysid of this ObservationsSummary.
        :type: str
        """
        if sysid is None:
            raise ValueError("Invalid value for `sysid`, must not be `None`")

        self._sysid = sysid

    @property
    def strid(self):
        """
        Gets the strid of this ObservationsSummary.

        :return: The strid of this ObservationsSummary.
        :rtype: str
        """
        return self._strid

    @strid.setter
    def strid(self, strid):
        """
        Sets the strid of this ObservationsSummary.

        :param strid: The strid of this ObservationsSummary.
        :type: str
        """
        if strid is None:
            raise ValueError("Invalid value for `strid`, must not be `None`")

        self._strid = strid

    @property
    def time(self):
        """
        Gets the time of this ObservationsSummary.

        :return: The time of this ObservationsSummary.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this ObservationsSummary.

        :param time: The time of this ObservationsSummary.
        :type: str
        """

        self._time = time

    @property
    def added(self):
        """
        Gets the added of this ObservationsSummary.

        :return: The added of this ObservationsSummary.
        :rtype: float
        """
        return self._added

    @added.setter
    def added(self, added):
        """
        Sets the added of this ObservationsSummary.

        :param added: The added of this ObservationsSummary.
        :type: float
        """

        self._added = added

    @property
    def removed(self):
        """
        Gets the removed of this ObservationsSummary.

        :return: The removed of this ObservationsSummary.
        :rtype: float
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """
        Sets the removed of this ObservationsSummary.

        :param removed: The removed of this ObservationsSummary.
        :type: float
        """

        self._removed = removed

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
        if not isinstance(other, ObservationsSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

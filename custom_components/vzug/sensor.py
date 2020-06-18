"""
V-ZUG Home Platform
"""
import logging
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import (PLATFORM_SCHEMA)

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the sensor platform"""
    _LOGGER.debug('in setup platform')
    add_devices([VZUGSensor()], True)

class VZUGSensor(Entity):
    """The class for this sensor"""
    def __init__(self):
        _LOGGER.debug('in init')
"""
The "vzug" custom component.
"""
import asyncio
import logging

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol

from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_IP_ADDRESS
)

DOMAIN = "vzug"

from vzug.vzug import VZUG

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_IP_ADDRESS): cv.string,
    vol.Required(CONF_USERNAME): cv.string,
    vol.Required(CONF_PASSWORD): cv.string,
})

async def async_setup(hass, config):
    hass.states.set('vzug.initializes', True)

    ip_address = config[CONF_IP_ADDRESS]
    username = config[CONF_USERNAME]
    password = config.get(CONF_PASSWORD)

    async with VZUG(ip_address, username, password) as vzug:
        # Collect the data of the current state
        await vzug.get_device_status()
        _LOGGER.debug("Device details %s", vzug.device_status)

    # Return boolean to indicate that initialization was successfully.
    return True
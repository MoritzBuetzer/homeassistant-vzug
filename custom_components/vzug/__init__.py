"""
The "vzug" custom component.
"""
import asyncio
import logging

import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
import voluptuous as vol

from homeassistant.const import (
    CONF_HOST,
    CONF_USERNAME,
    CONF_PASSWORD
)

DOMAIN = "vzug"
COMPONENT_DOMAIN = "vzug"

from vzug.vzug import VZUG

_LOGGER = logging.getLogger(__name__)

# Validation of the user's configuration
# CONFIG_SCHEMA = vol.Schema({
#     COMPONENT_DOMAIN: vol.Schema({
#         vol.Required(CONF_HOST): cv.string,
#         vol.Required(CONF_USERNAME): cv.string,
#         vol.Required(CONF_PASSWORD): cv.string
#     })
# })

async def async_setup(hass, config):
    hass.states.set('vzug.initializes', True)

    # host = config[CONF_HOST]
    # username = config[CONF_USERNAME]
    # password = config[CONF_PASSWORD]

    host = "192.168.x.x"
    username = "USERNAME"
    password = "PASSWORD"

    _LOGGER.debug("in async_setup")

    async with VZUG(host, username, password) as vzug:
        # Collect the data of the current state
        await vzug.get_device_status()
        _LOGGER.debug("Device details %s", vzug.device_status)

    # Return boolean to indicate that initialization was successfully.
    return True
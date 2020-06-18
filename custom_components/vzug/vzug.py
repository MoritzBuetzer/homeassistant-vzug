DOMAIN = "vzug"

def setup(hass, config):
    """Setup the vzug component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set("vzug.Hello_World", "Works!")

    # Return boolean to indicate that initialization was successfully.
    return True
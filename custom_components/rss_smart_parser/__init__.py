DOMAIN = "rss_smart_parser"

async def async_setup_entry(hass, entry):
    """Set up Smart RSS from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
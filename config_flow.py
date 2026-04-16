import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

DOMAIN = "rss_smart_parser"

class SmartRSSConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart RSS."""
    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title=user_input["name"], data=user_input)

        data_schema = vol.Schema({
            vol.Required("name", default="News feed"): str,
            vol.Required("url"): str,
            vol.Required("limit", default=5): vol.Coerce(int),
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
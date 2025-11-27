"""Adds config flow for Vacances Scolaires France."""

from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import selector
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from slugify import slugify

from .api import (
    VacancesFrApiClient,
)
from .const import CONF_ZONE, DOMAIN


class VacancesFrFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Vacances Scolaires France."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle a flow initialized by the user."""
        _errors = {}
        if user_input is not None:
            await self.async_set_unique_id(unique_id=slugify(user_input[CONF_ZONE]))
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=user_input[CONF_ZONE],
                data=user_input,
            )

        client = VacancesFrApiClient(session=async_get_clientsession(self.hass))
        zones = await client.async_get_zones()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("zone"): selector.SelectSelector({"options": zones}),
                }
            ),
            errors=_errors,
        )

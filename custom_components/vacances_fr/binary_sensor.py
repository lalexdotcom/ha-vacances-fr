"""Binary sensor platform for integration_blueprint."""

from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.const import Platform
from homeassistant.core import callback
from homeassistant.helpers.event import (
    async_track_time_change,
)
from homeassistant.util import dt, slugify

from .const import DOMAIN, FRIENDLY_PREFIX
from .data import get_period_extra_attributes
from .entity import VacancesFrEntity

if TYPE_CHECKING:
    from collections.abc import Callable

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import VacancesFrDataUpdateCoordinator
    from .data import VacancesFrConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: VacancesFrConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    async_add_entities(
        [
            VacancesFrTomorrowBinarySensor(
                coordinator=entry.runtime_data.coordinator,
                entity_description=BinarySensorEntityDescription(
                    key="vacances_fr_tomorrow",
                    name=f"{FRIENDLY_PREFIX} demain ?",
                ),
            )
        ]
    )


class VacancesFrTomorrowBinarySensor(VacancesFrEntity, BinarySensorEntity):
    """vacances_fr tomorrow binary_sensor class."""

    unsubscribe: Callable[[], None] | None = None

    def __init__(
        self,
        coordinator: VacancesFrDataUpdateCoordinator,
        entity_description: BinarySensorEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        self.entity_id = f"{Platform.BINARY_SENSOR}.{DOMAIN}_tomorrow_{
            slugify(self.coordinator.config_entry.data['zone'])
        }"
        self.entity_description = entity_description

    async def async_added_to_hass(self) -> None:
        """Subscribe to event each day at 00:00 to update value."""
        await super().async_added_to_hass()
        self.unsubscribe = async_track_time_change(
            self.hass, lambda _: self._handle_coordinator_update(), 0, 0, 0
        )

    async def async_will_remove_from_hass(self) -> None:
        """Unsubscribe from the events."""
        if self.unsubscribe:
            self.unsubscribe()
        await super().async_will_remove_from_hass()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Update the entity."""
        tomorrow_event = self.coordinator.get_date_event(
            dt.now().date() + timedelta(days=1)
        )
        if tomorrow_event is not None:
            self._attr_is_on = True
            self._attr_extra_state_attributes = get_period_extra_attributes(
                tomorrow_event
            )
        else:
            self._attr_is_on = False

        self.schedule_update_ha_state()

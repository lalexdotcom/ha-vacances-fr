"""Sensor platform for integration_blueprint."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.const import Platform
from homeassistant.core import callback
from homeassistant.helpers.event import async_track_time_change
from homeassistant.util import dt, slugify

from .const import DOMAIN, FRIENDLY_PREFIX
from .data import get_period_extra_attributes
from .entity import VacancesFrEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import VacancesFrDataUpdateCoordinator
    from .data import VacancesFrConfigEntry


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: VacancesFrConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        [
            CurrentVacancesFrSensor(
                coordinator=entry.runtime_data.coordinator,
            ),
            NextVacancesFrSensor(
                coordinator=entry.runtime_data.coordinator,
            ),
        ]
    )


class CurrentVacancesFrSensor(VacancesFrEntity, SensorEntity):
    """vacances_fr current Sensor class."""

    def __init__(
        self,
        coordinator: VacancesFrDataUpdateCoordinator,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_id = f"{Platform.SENSOR}.{DOMAIN}_current_{
            slugify(self.coordinator.config_entry.data['zone'])
        }"
        self.entity_description = SensorEntityDescription(
            key="vacances_fr_current",
            name=f"{FRIENDLY_PREFIX} en cours",
            icon="mdi:format-quote-close",
        )

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
        today_event = self.coordinator.get_date_event(dt.now().date())
        if today_event is not None:
            self._attr_native_value = today_event.summary
            self._attr_extra_state_attributes = get_period_extra_attributes(today_event)
        else:
            self._attr_native_value = None

        self.schedule_update_ha_state()


class NextVacancesFrSensor(VacancesFrEntity, SensorEntity):
    """vacances_fr current Sensor class."""

    def __init__(
        self,
        coordinator: VacancesFrDataUpdateCoordinator,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_id = f"{Platform.SENSOR}.{DOMAIN}_next_{
            slugify(self.coordinator.config_entry.data['zone'])
        }"
        self.entity_description = SensorEntityDescription(
            key="vacances_fr_next",
            name=f"{FRIENDLY_PREFIX} à venir",
            icon="mdi:format-quote-close",
        )

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
        today = dt.now().date()
        next_event = self.coordinator.get_date_future_event(today)
        if next_event is not None:
            self._attr_native_value = next_event.summary
            self._attr_extra_state_attributes = get_period_extra_attributes(next_event)
        else:
            self._attr_native_value = None

        self.schedule_update_ha_state()

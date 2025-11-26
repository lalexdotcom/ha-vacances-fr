"""Binary sensor platform for vacances_fr."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.calendar import (
    CalendarEntity,
    CalendarEntityDescription,
    CalendarEvent,
)
from homeassistant.const import Platform
from homeassistant.util import dt, slugify

from .const import DOMAIN, FRIENDLY_NAME
from .entity import VacancesFrEntity

if TYPE_CHECKING:
    from datetime import date, datetime

    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import VacancesFrDataUpdateCoordinator
    from .data import VacancesFrConfigEntry

ENTITY_DESCRIPTIONS = (
    CalendarEntityDescription(key="vacances_fr", name=FRIENDLY_NAME),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: VacancesFrConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary_sensor platform."""
    async_add_entities(
        VacancesFrCalendar(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class VacancesFrCalendar(VacancesFrEntity, CalendarEntity):
    """vacances_fr binary_sensor class."""

    def __init__(
        self,
        coordinator: VacancesFrDataUpdateCoordinator,
        entity_description: CalendarEntityDescription,
    ) -> None:
        """Initialize the binary_sensor class."""
        super().__init__(coordinator)
        zone = self.coordinator.config_entry.data["zone"]
        self._event: CalendarEvent | None = None
        self.entity_description = entity_description
        self.entity_id = f"{Platform.CALENDAR}.{DOMAIN}_{slugify(zone)}"

    @property
    def event(self) -> CalendarEvent | None:
        """Return the next upcoming event."""
        return self._event

    async def async_update(self) -> None:
        """Update the entity."""
        zone = self.coordinator.config_entry.data["zone"]

        def next_event() -> CalendarEvent | None:
            now = dt.now().date()
            events = (
                event
                for event in (
                    self.coordinator.data["holidays"]
                    if self.coordinator.data is not None
                    else []
                )
                if event["end"] >= now
            )
            if event := next(events, None):
                return CalendarEvent(
                    start=event["start"],
                    end=event["end"],
                    summary=f"{event['summary']} - {zone}",
                    uid=event["uid"],
                )
            return None

        self._event = await self.hass.async_add_executor_job(next_event)

    async def async_get_events(
        self,
        hass: HomeAssistant,  # noqa: ARG002
        start_date: datetime,
        end_date: datetime,
    ) -> list[CalendarEvent]:
        """Get events in a specific date range."""
        zone = self.coordinator.config_entry.data["zone"]
        events: list[CalendarEvent] = []
        for event in self.coordinator.data["holidays"]:
            event_start: date = event["start"]
            event_end: date = event["end"]

            if event_end >= start_date.date() and event_start <= end_date.date():
                summary = f"{event['summary']} - {zone}"
                events.append(
                    CalendarEvent(
                        summary=summary,
                        start=event_start,
                        end=event_end,
                        uid=event["uid"],
                    )
                )

        return events

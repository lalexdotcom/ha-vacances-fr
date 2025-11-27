"""Custom types for vacances_fr."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from datetime import date

    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import VacancesFrApiClient
    from .coordinator import VacancesFrDataUpdateCoordinator


type VacancesFrConfigEntry = ConfigEntry[VacancesFrData]


@dataclass
class VacancesFrData:
    """Data for the Vacances Scolaires France integration."""

    client: VacancesFrApiClient
    coordinator: VacancesFrDataUpdateCoordinator
    integration: Integration


@dataclass
class VacancesFrPeriod:
    """Data for the Vacances Scolaires France integration."""

    summary: str
    start: date
    end: date
    uid: str
    zone: str
    year: str


def get_period_extra_attributes(event: VacancesFrPeriod) -> dict[str, Any]:
    """Get extra attributes for an event."""
    return {
        "start_date": event.start,
        "end_date": event.end,
        "zone": event.zone,
        "année_scolaire": event.year,
    }

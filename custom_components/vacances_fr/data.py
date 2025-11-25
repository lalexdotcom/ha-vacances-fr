"""Custom types for vacances_fr."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import VacancesFrApiClient
    from .coordinator import VacancesFrDataUpdateCoordinator


type VacancesFrConfigEntry = ConfigEntry[VacancesFrData]


@dataclass
class VacancesFrData:
    """Data for the Vacances Scolaires FR integration."""

    client: VacancesFrApiClient
    coordinator: VacancesFrDataUpdateCoordinator
    integration: Integration

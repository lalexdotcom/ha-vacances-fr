"""Sample API Client."""

from __future__ import annotations

import socket
import urllib.parse
from datetime import datetime
from typing import Any

import aiohttp
import async_timeout


class VacancesFrApiClientError(Exception):
    """Exception to indicate a general API error."""


class VacancesFrApiClientCommunicationError(
    VacancesFrApiClientError,
):
    """Exception to indicate a communication error."""


class VacancesFrApiClientAuthenticationError(
    VacancesFrApiClientError,
):
    """Exception to indicate an authentication error."""


class VacancesFrApiClient:
    """API Client."""

    def __init__(
        self,
        session: aiohttp.ClientSession,
    ) -> None:
        """Sample API Client."""
        self._session = session

    async def async_get_zones(self) -> Any:
        """Get available zones from the API."""
        zones_result = await self._api_wrapper(
            method="get",
            url="https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-calendrier-scolaire/records?group_by=zones&order_by=zones&limit=100",
        )

        return sorted(
            [x["zones"] for x in zones_result["results"]],
            key=lambda s: "1" if s.startswith("Zone") else "2",
        )

    async def async_get_events(self, zone: str) -> Any:
        """Get data from the API."""
        today = datetime.now().date()  # noqa: DTZ005
        url = f"https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-calendrier-scolaire/records?limit=100&refine={
            urllib.parse.quote(f'zones:"{zone}"')
        }&where={
            urllib.parse.quote(f"end_date >= date'{today}' and end_date > start_date")
        }&timezone={urllib.parse.quote('Europe/Paris')}&refine={
            urllib.parse.quote('population:"-"')
        }&refine={urllib.parse.quote('population:"Élèves"')}&order_by={
            urllib.parse.quote('start_date,location')
        }&group_by={
            urllib.parse.quote('start_date,end_date,description,zones,annee_scolaire')
        }"

        events_result = await self._api_wrapper(
            method="get",
            url=url,
        )

        return events_result["results"]

    async def _api_wrapper(
        self,
        method: str,
        url: str,
        data: dict | None = None,
        headers: dict | None = None,
    ) -> Any:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(10):
                response = await self._session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    json=data,
                )
                return await response.json()

        except TimeoutError as exception:
            msg = f"Timeout error fetching information - {exception}"
            raise VacancesFrApiClientCommunicationError(
                msg,
            ) from exception
        except (aiohttp.ClientError, socket.gaierror) as exception:
            msg = f"Error fetching information - {exception}"
            raise VacancesFrApiClientCommunicationError(
                msg,
            ) from exception
        except Exception as exception:  # pylint: disable=broad-except
            msg = f"Something really wrong happened! - {exception}"
            raise VacancesFrApiClientError(
                msg,
            ) from exception

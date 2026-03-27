from __future__ import annotations

from typing import Any

from pydantic import field_validator

from desslyhub.enums import TransactionStatus
from desslyhub.types.base import DesslyHubObject


__all__ = (
    "MobileGame",
    "MobileGameDetails",
    "MobileGameList",
    "MobileGamePosition",
    "MobileGameRefill",
)


class MobileGame(DesslyHubObject):
    name: str
    """Game name"""
    id: int
    """Game ID"""


class MobileGameList(DesslyHubObject):
    games: list[MobileGame]
    """List of games available for top-up"""


class MobileGamePosition(DesslyHubObject):
    id: int
    """Position ID (used for specifying the position in top-up requests)"""
    name: str
    """Position name (e.g., "100 coins", "500 coins", etc.)"""
    price: float
    """Price of the position"""


class MobileGameDetails(DesslyHubObject):
    id: int
    """Game ID"""
    name: str
    """Game name"""
    servers: dict[str, str]
    """
    Available servers for the game (key: server ID, value: server name). If the game does not have servers, this will be an empty dictionary
    """  # noqa: E501
    fields: dict[str, Any]
    """
    Additional fields required for top-up (key: field name, value: field description). If the game does not require additional fields, this will be an empty dictionary
    """  # noqa: E501
    positions: list[MobileGamePosition]
    """
    Available top-up positions for the game. If the game does not have predefined positions, this will be an empty list
    """  # noqa: E501

    @field_validator("servers", mode="before")
    @classmethod
    def validate_servers(cls, value: dict[str, str] | None) -> dict[str, str]:
        if value is None:
            return {}
        return value


class MobileGameRefill(DesslyHubObject):
    transaction_id: str | None = None
    """The transaction ID you specified in your request"""
    status: TransactionStatus
    """Transaction status"""

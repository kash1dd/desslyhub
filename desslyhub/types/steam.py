from __future__ import annotations

from pydantic import Field

from desslyhub.enums import TransactionStatus
from desslyhub.types.base import DesslyHubObject


__all__ = (
    "CheckSteamLogin",
    "GameDetails",
    "RegionInfo",
    "SendSteamGiftGame",
    "SteamGame",
    "SteamGameDetailsList",
    "SteamGameList",
    "SteamTopUp",
)


class CheckSteamLogin(DesslyHubObject):
    can_refill: bool
    """Indicates whether the provided Steam login can be used for top-up or gift purchases"""


class SteamTopUp(DesslyHubObject):
    transaction_id: str
    """The transaction ID you specified in your request"""
    status: TransactionStatus
    """transaction status"""


class SteamGame(DesslyHubObject):
    name: str
    """Game name"""
    app_id: int = Field(alias="appid")
    """Game app ID"""


class SteamGameList(DesslyHubObject):
    games: list[SteamGame]
    """List of games available for purchase as gifts"""


class RegionInfo(DesslyHubObject):
    region: str
    """Region code (ISO 3166-2)"""
    discount: int
    """Discount percentage for the game in this region"""
    price: float
    """Price of the game in this region after applying the discount"""
    price_original: float
    """Original price of the game in this region before applying the discount"""


class GameDetails(DesslyHubObject):
    edition: str
    """Game edition name (e.g., Standard, Deluxe, etc.)"""
    package_id: int
    """Package ID required for purchasing the game as a gift"""
    regions_info: list[RegionInfo]
    """
    List of regions where the game is available for purchase as a gift, along with pricing information
    """  # noqa: E501


class SteamGameDetailsList(DesslyHubObject):
    game: list[GameDetails]
    """List of game editions available for purchase as gifts"""


class SendSteamGiftGame(DesslyHubObject):
    transaction_id: str | None = None
    """The transaction ID you specified in your request"""
    status: TransactionStatus
    """Transaction status"""

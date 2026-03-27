from __future__ import annotations

from http import HTTPMethod

from desslyhub.types.steam import SteamTopUp
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("SteamTopUpMethod",)


class SteamTopUpMethod(DesslyHubMethod[SteamTopUp]):
    """
    Top up a Steam account.

    Source: https://desslyhub.readme.io/reference/post_apiv1servicesteamtopuptopup
    """

    __api_method__: str = "v1/service/steamtopup/topup"
    __http_method__: HTTPMethod = HTTPMethod.POST
    __return_type__: type[SteamTopUp] = SteamTopUp

    amount: float
    """Deposit amount in USD,ranging from 0.1 to 1000"""
    username: str
    """User login steam"""
    reference: str | None = None
    """your ID, if necessary"""

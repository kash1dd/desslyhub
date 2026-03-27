from __future__ import annotations

from http import HTTPMethod

from desslyhub.types.steam import CheckSteamLogin
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("CheckSteamLoginMethod",)


class CheckSteamLoginMethod(DesslyHubMethod[CheckSteamLogin]):
    """
    Check if a Steam account can be topped up.

    Source: https://desslyhub.readme.io/reference/post_apiv1servicesteamtopupcheck_login
    """

    __api_method__: str = "v1/service/steamtopup/check_login"
    __http_method__: HTTPMethod = HTTPMethod.POST
    __return_type__: type[CheckSteamLogin] = CheckSteamLogin

    amount: float
    """Deposit amount in USD, ranging from 0.1 to 1000"""
    username: str
    """Steam user login"""

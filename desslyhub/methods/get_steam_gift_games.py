from __future__ import annotations

from http import HTTPMethod

from desslyhub.types.steam import SteamGameList
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("GetSteamGiftGamesMethod",)


class GetSteamGiftGamesMethod(DesslyHubMethod[SteamGameList]):
    """
    Obtaining a list of games available for purchase

    Source: https://desslyhub.readme.io/reference/get_apiv1steamgames
    """

    __api_method__: str = "v1/service/steamgift/games"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[SteamGameList] = SteamGameList

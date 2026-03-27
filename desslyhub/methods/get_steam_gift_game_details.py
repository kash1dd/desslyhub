from __future__ import annotations

from http import HTTPMethod

from desslyhub.types.steam import SteamGameDetailsList
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("GetSteamGiftGameDetailsMethod",)


class GetSteamGiftGameDetailsMethod(DesslyHubMethod[SteamGameDetailsList]):
    """
    Obtaining information about specific editions of the game by its app_id

    Source: https://desslyhub.readme.io/reference/get_apiv1steamgamesapp_id
    """

    __api_method__: str = "v1/service/steamgift/games/{app_id}"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[SteamGameDetailsList] = SteamGameDetailsList

    def __init__(self, app_id: int) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(app_id=app_id)

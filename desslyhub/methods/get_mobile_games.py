from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.mobile import MobileGameList


__all__ = ("GetMobileGamesMethod",)


class GetMobileGamesMethod(DesslyHubMethod[MobileGameList]):
    """
    Obtaining a list of games available for replenishment, indicating the source option.

    Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgames
    """

    __api_method__: str = "v1/service/mobile/variant/{variant}/games"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[MobileGameList] = MobileGameList

    def __init__(self, variant: str) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(variant=variant)

from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.mobile import MobileGameDetails


__all__ = ("GetMobileGameDetailsMethod",)


class GetMobileGameDetailsMethod(DesslyHubMethod[MobileGameDetails]):
    """
    Obtaining information about a specific game by its identifier, indicating the source option.

    Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgamesid
    """

    __api_method__: str = "v1/service/mobile/variant/{variant}/games/{game_id}"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[MobileGameDetails] = MobileGameDetails

    def __init__(self, variant: str, game_id: str) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(variant=variant, game_id=game_id)

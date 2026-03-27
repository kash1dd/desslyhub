from __future__ import annotations

from typing import Any
from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.mobile import MobileGameRefill


__all__ = ("SendMobileGameRefillMethod",)


class SendMobileGameRefillMethod(DesslyHubMethod[MobileGameRefill]):
    """
    Mobile game top-ups with a choice of payment source.

    Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgamesrefill
    """

    __api_method__: str = "v1/service/mobile/variant/{variant}/games/refill"
    __http_method__: HTTPMethod = HTTPMethod.POST
    __return_type__: type[MobileGameRefill] = MobileGameRefill

    fields: dict[str, str]
    """key-value data set specified when obtaining game information on the Get Game By ID handle"""
    position: int
    """	ID of a specific position, obtained in Get Game By App ID for a specific game"""
    reference: str | None = None
    """your ID , if necessary"""

    def __init__(self, variant: str, **data: Any) -> None:
        super().__init__(**data)
        self.__api_method__ = self.__api_method__.format(variant=variant)

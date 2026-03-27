from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.exchange_rate import SteamExchangeRate


__all__ = ("GetSteamExchangeRateMethod",)


class GetSteamExchangeRateMethod(DesslyHubMethod[SteamExchangeRate]):
    """
    Obtaining the exchange rate for a specific currency.

    Source: https://desslyhub.readme.io/reference/get-exchange-rate
    """

    __api_method__: str = "v1/exchange_rate/steam/{currency}"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[SteamExchangeRate] = SteamExchangeRate

    def __init__(self, currency: int) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(currency=currency)

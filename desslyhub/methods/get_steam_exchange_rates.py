from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.exchange_rate import SteamExchangeRates


__all__ = ("GetSteamExchangeRatesMethod",)


class GetSteamExchangeRatesMethod(DesslyHubMethod[SteamExchangeRates]):
    """
    Obtaining exchange rates for all supported currencies.

    Source: https://desslyhub.readme.io/reference/get-all-exchange-rates
    """

    __api_method__: str = "v1/exchange_rates/steam"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[SteamExchangeRates] = SteamExchangeRates

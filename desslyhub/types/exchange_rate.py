from __future__ import annotations

from pydantic import field_validator

from desslyhub.enums import Currency
from desslyhub.types.base import DesslyHubObject


__all__ = (
    "SteamExchangeRate",
    "SteamExchangeRates",
)


class SteamExchangeRate(DesslyHubObject):
    exchange_rate: float
    """Exchange rate for the specified currency"""


class SteamExchangeRates(DesslyHubObject):
    exchange_rates: dict[Currency, float]
    """Exchange rates for all supported currencies"""

    @field_validator("exchange_rates", mode="before")
    @classmethod
    def parse_exchange_rates(cls, v: dict[str, float]) -> dict[Currency, float]:
        return {Currency(int(k)): val for k, val in v.items()}

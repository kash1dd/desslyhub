from __future__ import annotations

import pytest
from desslyhub.enums import Currency
from desslyhub.types.exchange_rate import SteamExchangeRates


VALID_CASES = [
    {
        "exchange_rates": {
            "1": 1,
            "2": 0.7425,
            "3": 85.6653,
        }
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_steam_exchange_rates_model(data: dict):
    result = SteamExchangeRates.model_validate(data)
    assert isinstance(result.exchange_rates, dict)
    assert result.exchange_rates[Currency.USD] == 1
    assert result.exchange_rates[Currency.GBP] == 0.7425
    assert result.exchange_rates[Currency.EUR] == 85.6653
    assert all(isinstance(k, Currency) for k in result.exchange_rates)
    assert all(isinstance(v, float) for v in result.exchange_rates.values())

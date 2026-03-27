from __future__ import annotations

import pytest
from desslyhub.types.exchange_rate import SteamExchangeRate


VALID_CASES = [
    {"exchange_rate": 87.87},
    {"exchange_rate": 1.0},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_steam_exchange_rate_model(data: dict):
    result = SteamExchangeRate.model_validate(data)
    assert result.exchange_rate == data["exchange_rate"]

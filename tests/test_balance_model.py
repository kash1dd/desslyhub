from __future__ import annotations

import pytest
from desslyhub.types import Balance


VALID_CASES = [
    {"balance": "100.0"},
    {"balance": 100.0},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_balance_model(data: dict[str, str | int]):
    Balance.model_validate(data)

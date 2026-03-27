from __future__ import annotations

import pytest
from desslyhub.types.mobile import MobileGameRefill


VALID_CASES = [
    {
        "transaction_id": "6ddaf262-14c0-4ba4-b782-8839895ff642",
        "status": "pending",
        "error_code": 0,
    },
    {
        "status": "pending",
        "error_code": 0,
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_mobile_game_refill_model(data: dict):
    result = MobileGameRefill.model_validate(data)
    assert result.status == data["status"]
    assert result.error_code == data["error_code"]
    assert result.transaction_id == data.get("transaction_id")

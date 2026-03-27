from __future__ import annotations

import pytest
from desslyhub.types.steam import SteamTopUp


VALID_CASES = [
    {"transaction_id": "6ddaf262-14c0-4ba4-b782-8839895ff642", "status": "pending"},
    {"transaction_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "status": "success"},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_steam_top_up_model(data: dict[str, str]):
    result = SteamTopUp.model_validate(data)
    assert result.transaction_id == data["transaction_id"]
    assert result.status == data["status"]

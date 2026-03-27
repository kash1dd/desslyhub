from __future__ import annotations

import pytest
from desslyhub.types.steam import SendSteamGiftGame


VALID_CASES = [
    {
        "transaction_id": "6ddaf262-14c0-4ba4-b782-8839895ff642",
        "status": "pending",
        "error_code": 0,
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_send_steam_gift_game_model(data: dict):
    result = SendSteamGiftGame.model_validate(data)
    assert result.transaction_id == data["transaction_id"]
    assert result.status == data["status"]
    assert result.error_code == data["error_code"]

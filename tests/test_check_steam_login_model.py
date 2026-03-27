from __future__ import annotations

import pytest
from desslyhub.types.steam import CheckSteamLogin


VALID_CASES = [
    {"can_refill": "true"},
    {"can_refill": "false"},
    {"can_refill": True},
    {"can_refill": False},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_check_steam_login_model(data: dict[str, str | bool]):
    result = CheckSteamLogin.model_validate(data)
    if isinstance(data["can_refill"], str):
        assert result.can_refill == (data["can_refill"] == "true")
    else:
        assert result.can_refill == data["can_refill"]

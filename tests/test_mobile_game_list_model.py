from __future__ import annotations

import pytest
from desslyhub.types.mobile import MobileGameList


VALID_CASES = [
    {
        "games": [
            {"name": "Game Name 1", "id": 123456},
            {"name": "Game Name 2", "id": 234567},
        ]
    },
    {"games": []},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_mobile_game_list_model(data: dict):
    result = MobileGameList.model_validate(data)
    assert len(result.games) == len(data["games"])
    for game, expected in zip(result.games, data["games"]):
        assert game.name == expected["name"]
        assert game.id == expected["id"]

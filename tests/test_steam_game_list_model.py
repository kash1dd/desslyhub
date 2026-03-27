from __future__ import annotations

import pytest
from desslyhub.types.steam import SteamGameList


VALID_CASES = [
    {
        "games": [
            {"name": "Game Name 1", "appid": 123456},
            {"name": "Game Name 2", "appid": 234567},
        ]
    },
    {"games": []},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_steam_game_list_model(data: dict):
    result = SteamGameList.model_validate(data)
    assert len(result.games) == len(data["games"])
    for game, expected in zip(result.games, data["games"]):
        assert game.name == expected["name"]
        assert game.appid == expected["appid"]

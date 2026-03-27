from __future__ import annotations

import pytest
from desslyhub.types.mobile import MobileGameDetails


VALID_CASES = [
    {
        "id": 14,
        "name": "PUBG Mobile (Global)",
        "servers": {},
        "fields": {"Player ID": "Player ID"},
        "positions": [
            {"id": 22, "name": "1500 + 300 Extra UC", "price": "21.9000"},
            {"id": 23, "name": "3000 + 850 Extra UC", "price": "43.6400"},
            {"id": 20, "name": "300 + 25 Extra UC", "price": "4.4200"},
        ],
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_mobile_game_details_model(data: dict):
    result = MobileGameDetails.model_validate(data)
    assert result.id == data["id"]
    assert result.name == data["name"]
    assert result.servers == data["servers"]
    assert result.fields == data["fields"]
    assert len(result.positions) == len(data["positions"])
    assert result.positions[0].id == 22
    assert result.positions[0].name == "1500 + 300 Extra UC"
    assert result.positions[0].price == "21.9000"

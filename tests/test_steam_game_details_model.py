from __future__ import annotations

import pytest
from desslyhub.types.steam import SteamGameDetailsList


VALID_CASES = [
    {
        "game": [
            {
                "edition": "Edition Name",
                "package_id": 456432,
                "regions_info": [
                    {
                        "region": "RU",
                        "discount": "94",
                        "price": "3.6290",
                        "price_original": "33.6290",
                    },
                    {
                        "region": "BR",
                        "discount": "10",
                        "price": "4.2655",
                        "price_original": "42.2655",
                    },
                ],
            }
        ]
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_steam_game_details_model(data: dict):
    result = SteamGameDetailsList.model_validate(data)
    assert len(result.game) == len(data["game"])
    assert result.game[0].edition == "Edition Name"
    assert result.game[0].package_id == 456432
    assert len(result.game[0].regions_info) == 2
    assert result.game[0].regions_info[0].region == "RU"

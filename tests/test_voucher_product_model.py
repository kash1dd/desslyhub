from __future__ import annotations

import pytest
from desslyhub.types.voucher import VoucherProduct


VALID_CASES = [
    {
        "id": 797,
        "name": "Adobe Digital Code",
        "country": "AE",
        "variations": [
            {
                "id": 5107,
                "name": "Adobe Acrobat AI Assistant: 1 Year",
                "voucher_currency": "USD",
                "price": "51.4633",
                "stock": 1,
                "benefits": "Subscription",
            },
            {
                "id": 5113,
                "name": "Adobe Creative Cloud Photography: 1 Year Plan",
                "voucher_currency": "USD",
                "price": "206.0761",
                "stock": 1,
                "benefits": "Subscription",
            },
        ],
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_voucher_product_model(data: dict):
    result = VoucherProduct.model_validate(data)
    assert result.id == data["id"]
    assert result.name == data["name"]
    assert result.country == data["country"]
    assert len(result.variations) == len(data["variations"])
    assert result.variations[0].id == 5107
    assert result.variations[0].voucher_currency == "USD"
    assert result.variations[0].stock == 1

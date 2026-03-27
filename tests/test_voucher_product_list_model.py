from __future__ import annotations

import pytest
from desslyhub.types.voucher import VoucherProductList


VALID_CASES = [
    {
        "products": [
            {
                "id": 1024,
                "name": "7 Days to Die | GL",
                "country": "GLOB",
                "variations": [
                    {
                        "id": 6278,
                        "name": "7 Days to Die",
                        "voucher_currency": "USD",
                        "price": "18.1000",
                        "stock": 3,
                        "benefits": "Game",
                    }
                ],
            },
            {
                "id": 879,
                "name": "A1 Voucher | AT",
                "country": "AT",
                "variations": [
                    {
                        "id": 5566,
                        "name": "EUR 10 A1 Voucher",
                        "voucher_currency": "EUR",
                        "price": "11.7700",
                        "stock": 2,
                        "benefits": "Prepaid credit",
                    },
                    {
                        "id": 5567,
                        "name": "EUR 20 A1 Voucher",
                        "voucher_currency": "EUR",
                        "price": "23.5400",
                        "stock": 1,
                        "benefits": "Prepaid credit",
                    },
                ],
            },
        ]
    },
    {"products": []},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_voucher_product_list_model(data: dict):
    result = VoucherProductList.model_validate(data)
    assert len(result.products) == len(data["products"])
    for product, expected in zip(result.products, data["products"]):
        assert product.id == expected["id"]
        assert product.name == expected["name"]
        assert product.country == expected["country"]
        assert len(product.variations) == len(expected["variations"])

from __future__ import annotations

import pytest
from desslyhub.types.voucher import BuyVoucher


VALID_CASES = [
    {
        "transaction_uuid": "97945ca7-312c-4cc9-97fb-f27d07b81bff",
        "status": "success",
        "vouchers": [
            {
                "serialNumber": "123456",
                "pin": "zauvutfeq2wq237dm",
                "expiration": "2006-01-02 15:04:05",
            }
        ],
    },
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_buy_voucher_model(data: dict):
    result = BuyVoucher.model_validate(data)
    assert result.transaction_uuid == data["transaction_uuid"]
    assert result.status == data["status"]
    assert len(result.vouchers) == 1
    assert result.vouchers[0].serial_number == "123456"
    assert result.vouchers[0].pin == "zauvutfeq2wq237dm"
    assert result.vouchers[0].expiration == "2006-01-02 15:04:05"

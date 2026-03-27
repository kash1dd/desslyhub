from __future__ import annotations

import pytest
from desslyhub.types import Transaction


VALID_CASES = [
    {
        "transaction_id": "6ddaf262-14c0-4ba4-b782-8839895ff642",
        "status": "success",
        "attributes": "login",
        "amount": "0.1000",
        "commission": "0.0010",
        "final_amount": "0.1010",
        "type": "steam_refill",
        "created_at": "2025-07-16T22:15:00.651307+07:00",
        "updated_at": "2025-07-16T22:15:45.815131+07:00",
        "description": "refill steam",
    },
]


@pytest.mark.parametrize("transaction_data", VALID_CASES)
def test_transaction_model_valid(transaction_data):
    Transaction.model_validate(transaction_data)

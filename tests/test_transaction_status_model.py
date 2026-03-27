from __future__ import annotations

import pytest
from desslyhub.types import TransactionStatus


VALID_CASES = [
    {"status": "success"},
]


@pytest.mark.parametrize("data", VALID_CASES)
def test_transaction_status_model(data: dict[str, str]):
    TransactionStatus.model_validate(data)

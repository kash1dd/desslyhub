from __future__ import annotations

from datetime import datetime

from pydantic import Field

from desslyhub.enums import TransactionStatus as TransactionStatusEnum
from desslyhub.types.base import DesslyHubObject


__all__ = (
    "Transaction",
    "TransactionList",
    "TransactionStatus",
)


class Transaction(DesslyHubObject):
    id: str = Field(alias="transaction_id")
    """The transaction ID you specified in your request"""

    status: TransactionStatusEnum
    """transaction status"""

    attributes: str
    """Steam user login"""

    amount: str
    """the amount required to be credited to your Steam account"""

    commission: str
    """commission/discount for purchase"""

    final_amount: str
    """total top-up cost (amount to be debited from your balance)"""

    type: str
    """transaction type"""

    created_at: datetime
    """transaction creation date"""

    updated_at: datetime
    """transaction modification date"""

    description: str
    """transaction description"""


class TransactionList(DesslyHubObject):
    transactions: list[Transaction]
    """list of transactions"""

    count: int
    """number of transactions on the page received"""


class TransactionStatus(DesslyHubObject):
    status: TransactionStatusEnum
    """transaction status"""

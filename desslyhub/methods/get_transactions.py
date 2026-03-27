from __future__ import annotations

from http import HTTPMethod

from desslyhub.types import TransactionList
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("GetTransactionsMethod",)


class GetTransactionsMethod(DesslyHubMethod[TransactionList]):
    """
    Receiving all transactions page by page
    Transactions are returned page by page, starting with the most recent ones. 100 transactions per request. If the page number exceeds the number of your transactions, an empty list will be returned.

    Source: https://desslyhub.readme.io/reference/get_transactions
    """  # noqa: E501

    page: int = 1
    """Transaction page number. Counting starts from 1."""

    __api_method__: str = "v1/merchants/transactions"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[TransactionList] = TransactionList

from __future__ import annotations

from http import HTTPMethod

from desslyhub.types import Transaction
from desslyhub.methods.base import DesslyHubMethod


class GetTransactionMethod(DesslyHubMethod[Transaction]):
    """
    Retrieving a single transaction by id

    Source: https://desslyhub.readme.io/reference/get_apiv1transaction
    """

    __api_method__: str = "v1/merchants/transactions/{transaction_id}"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[Transaction] = Transaction

    def __init__(self, transaction_id: str) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(transaction_id=transaction_id)

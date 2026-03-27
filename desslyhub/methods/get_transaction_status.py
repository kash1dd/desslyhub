from __future__ import annotations

from http import HTTPMethod

from desslyhub.types import TransactionStatus
from desslyhub.methods.base import DesslyHubMethod


class GetTransactionStatusMethod(DesslyHubMethod[TransactionStatus]):
    """
    Checking transaction status

    Source: https://desslyhub.readme.io/reference/get_apiv1statustransaction_id
    """

    __api_method__: str = "v1/merchants/transactions/{transaction_id}/status"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[TransactionStatus] = TransactionStatus

    def __init__(self, transaction_id: str) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(transaction_id=transaction_id)

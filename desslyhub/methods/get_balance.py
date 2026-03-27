from __future__ import annotations

from http import HTTPMethod

from desslyhub.types import Balance
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("GetBalanceMethod",)


class GetBalanceMethod(DesslyHubMethod[Balance]):
    """
    Receiving a merchant balance

    Source: https://desslyhub.readme.io/reference/put_apiv1merchantsbalance
    """

    __api_method__: str = "v1/merchants/balance"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[Balance] = Balance

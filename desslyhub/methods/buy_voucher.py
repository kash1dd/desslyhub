from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.voucher import BuyVoucher


__all__ = ("BuyVoucherMethod",)


class BuyVoucherMethod(DesslyHubMethod[BuyVoucher]):
    """
    Purchasing a voucher

    Source: https://desslyhub.readme.io/reference/buy_voucher
    """

    __api_method__: str = "v1/service/voucher/buy"
    __http_method__: HTTPMethod = HTTPMethod.POST
    __return_type__: type[BuyVoucher] = BuyVoucher

    root_id: int
    """ID of a specific voucher obtained in Get Vouchers or Get Voucher By ID"""
    variant_id: int
    """ID of a specific variant obtained in Get Vouchers or Get Voucher By ID"""
    reference: str | None = None
    """Your ID, if necessary"""

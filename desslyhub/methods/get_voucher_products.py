from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.voucher import VoucherProductList


__all__ = ("GetVoucherProductsMethod",)


class GetVoucherProductsMethod(DesslyHubMethod[VoucherProductList]):
    """
    Obtaining information about vouchers

    Source: https://desslyhub.readme.io/reference/get_voucher_products
    """

    __api_method__: str = "v1/service/voucher/products"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[VoucherProductList] = VoucherProductList

from __future__ import annotations

from http import HTTPMethod

from desslyhub.methods.base import DesslyHubMethod
from desslyhub.types.voucher import VoucherProduct


__all__ = ("GetVoucherProductMethod",)


class GetVoucherProductMethod(DesslyHubMethod[VoucherProduct]):
    """
    Obtaining information about a specific voucher by its identifier

    Source: https://desslyhub.readme.io/reference/get_voucher_by_id
    """

    __api_method__: str = "v1/service/voucher/products/{product_id}"
    __http_method__: HTTPMethod = HTTPMethod.GET
    __return_type__: type[VoucherProduct] = VoucherProduct

    def __init__(self, product_id: int) -> None:
        super().__init__()
        self.__api_method__ = self.__api_method__.format(product_id=product_id)

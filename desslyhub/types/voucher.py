from __future__ import annotations

from pydantic import Field

from desslyhub.enums import TransactionStatus
from desslyhub.types.base import DesslyHubObject


__all__ = (
    "BuyVoucher",
    "Voucher",
    "VoucherProduct",
    "VoucherProductList",
    "VoucherVariation",
)


class VoucherVariation(DesslyHubObject):
    id: int
    """Variation voucher ID"""
    name: str
    """Variation voucher name"""
    voucher_currency: str
    """Currency of voucher application"""
    price: str
    """Price for the refill including discounts/commissions"""
    stock: int
    """Number of vouchers available"""
    benefits: str
    """Voucher description"""


class VoucherProduct(DesslyHubObject):
    id: int
    """Root voucher ID"""
    name: str
    """Voucher name"""
    country: str
    """Country for voucher redemption"""
    variations: list[VoucherVariation]
    """Available options for purchase"""


class VoucherProductList(DesslyHubObject):
    products: list[VoucherProduct]
    """List of voucher products"""


class Voucher(DesslyHubObject):
    serial_number: str = Field(alias="serialNumber")
    """Voucher serial number (can be used for accounting or activation, may be blank)"""
    pin: str
    """The PIN code of the voucher, which must be entered during activation"""
    expiration: str
    """Voucher expiration date and time (may be blank)"""


class BuyVoucher(DesslyHubObject):
    transaction_uuid: str
    """Transaction UUID"""
    status: TransactionStatus
    """Transaction status"""
    vouchers: list[Voucher]
    """List of purchased vouchers"""

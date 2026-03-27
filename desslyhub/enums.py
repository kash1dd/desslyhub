from __future__ import annotations

from enum import IntEnum, StrEnum


__all__ = ("TransactionStatus", "Variant", "Currency")


class TransactionStatus(StrEnum):
    SUCCESS = "success"
    """
    If the status is “success,” it means that the transaction went through and the money was debited.
    """  # noqa: E501

    PENDING = "pending"
    """
    If the status is "pending", it means that the transaction is being processed.
    """

    FAILED = "failed"
    """
    If the status is "failed", it means that the transaction ended with an error. The money has been returned to your account.
    """  # noqa: E501

    CANCELLED = "cancelled"
    """
    If the status is "cancelled", it means that the transaction has been canceled. The money has been returned to your account.
    """  # noqa: E501


class Variant(StrEnum):
    PROVIDER_1 = "1"
    """
    Provider 1
    """

    PROVIDER_2 = "2"
    """
    Provider 2
    """


class Currency(IntEnum):
    USD = 1
    """United States dollar"""

    GBP = 2
    """Pound sterling"""

    EUR = 3
    """Euro"""

    CHF = 4
    """Swiss franc"""

    RUB = 5
    """Russian ruble"""

    PLN = 6
    """Polish zloty"""

    BRL = 7
    """Brazilian real"""

    JPY = 8
    """Japanese yen"""

    NOK = 9
    """Norwegian krone"""

    IDR = 10
    """Indonesian rupiah"""

    MYR = 11
    """Malaysian ringgit"""

    PHP = 12
    """Philippine peso"""

    SGD = 13
    """Singapore dollar"""

    THB = 14
    """Thai baht"""

    VND = 15
    """Vietnamese dong"""

    KRW = 16
    """South Korean won"""

    UAH = 18
    """Ukrainian hryvnia"""

    MXN = 19
    """Mexican peso"""

    CAD = 20
    """Canadian dollar"""

    AUD = 21
    """Australian dollar"""

    NZD = 22
    """New Zealand dollar"""

    CNY = 23
    """Chinese yuan"""

    INR = 24
    """Indian rupee"""

    CLP = 25
    """Chilean peso"""

    PEN = 26
    """Peruvian sol"""

    COP = 27
    """Colombian peso"""

    ZAR = 28
    """South African rand"""

    HKD = 29
    """Hong Kong dollar"""

    TWD = 30
    """New Taiwan dollar"""

    SAR = 31
    """Saudi riyal"""

    AED = 32
    """UAE dirham"""

    ILS = 35
    """Israeli new shekel"""

    KZT = 37
    """Kazakhstani tenge"""

    KWD = 38
    """Kuwaiti dinar"""

    QAR = 39
    """Qatari riyal"""

    CRC = 40
    """Costa Rican colon"""

    UYU = 41
    """Uruguayan peso"""

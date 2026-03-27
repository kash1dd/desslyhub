from __future__ import annotations

from desslyhub.types.base import DesslyHubObject


__all__ = ("Balance",)


class Balance(DesslyHubObject):
    balance: float
    """Your current balance in USD"""

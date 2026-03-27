from __future__ import annotations

from typing import Any
from dataclasses import dataclass
from abc import ABC, abstractmethod

from desslyhub.methods import DesslyHubMethod
from desslyhub.exceptions import DesslyHubAPIError


__all__ = (
    "BaseSession",
    "RawResponse",
)

ERRORS: dict[int, type[DesslyHubAPIError]] = {
    cls.code: cls for cls in DesslyHubAPIError.__subclasses__()
}


@dataclass(frozen=True, slots=True)
class RawResponse:
    status_code: int
    error_code: int | None
    json: dict[str, Any] | list[Any] | None
    text: str | None


class BaseSession(ABC):
    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://desslyhub.com/api/",
    ) -> None:
        self._api_key = api_key
        self._base_url = base_url

    @property
    def api_key(self) -> str:
        return self._api_key

    @property
    def base_url(self) -> str:
        return self._base_url

    @staticmethod
    def raise_for_code(code: int) -> None:
        error_cls = ERRORS.get(code)
        if error_cls is not None:
            raise error_cls()

    @abstractmethod
    async def request(self, method: DesslyHubMethod[Any]) -> RawResponse: ...

    async def close(self) -> None: ...

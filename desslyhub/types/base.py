from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict


if TYPE_CHECKING:
    from desslyhub import Client


__all__ = ("DesslyHubObject",)


class DesslyHubObject(BaseModel):
    _client: Client | None = None

    model_config = ConfigDict(
        extra="allow",
        frozen=True,
    )

    def model_post_init(self, context: Any, /) -> None:
        if isinstance(context, dict):
            self._client: Client | None = context.get("client")

    @property
    def client(self) -> Client:
        if self._client is None:
            raise RuntimeError("Client is not set for this object.")
        return self._client

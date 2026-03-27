from __future__ import annotations

from typing import Any

from aiohttp import ClientSession

from desslyhub.methods import DesslyHubMethod
from desslyhub.client.session import RawResponse
from desslyhub.client.session.base import BaseSession


__all__ = ("AiohttpSession",)


class AiohttpSession(BaseSession):
    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://desslyhub.com/api/",
    ) -> None:
        super().__init__(
            api_key=api_key,
            base_url=base_url,
        )
        self._session: ClientSession | None = None

    def get_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                headers={"apikey": self.api_key},
                base_url=self.base_url,
            )

        return self._session

    async def close(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()

    async def request(self, method: DesslyHubMethod[Any]) -> RawResponse:
        session: ClientSession = self.get_session()
        request_body = method.get_request_body()

        async with session.request(
            method=method.__http_method__,
            url=method.__api_method__,
            json=request_body if method.__http_method__ in ("POST", "PUT", "PATCH") else None,
            params=request_body if method.__http_method__ in ("GET", "DELETE") else None,
        ) as response:
            text = await response.text()
            try:
                json = await response.json()
            except Exception:
                json = None

            raw_response = RawResponse(
                status_code=response.status,
                error_code=json.get("error_code") if isinstance(json, dict) else None,
                json=json,
                text=text,
            )
            self.raise_for_code(raw_response.error_code)
            return raw_response

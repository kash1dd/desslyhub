from __future__ import annotations

from typing import TYPE_CHECKING, Any, Generic
from abc import ABC
from http import HTTPMethod

from pydantic import BaseModel
from typing_extensions import TypeVar


if TYPE_CHECKING:
    from desslyhub.client.client import Client
    from desslyhub.client.session import RawResponse

__all__ = ("DesslyHubMethod",)

MethodReturnType = TypeVar("MethodReturnType", bound=Any)


class DesslyHubMethod(ABC, BaseModel, Generic[MethodReturnType]):
    __api_method__: str
    __http_method__: HTTPMethod
    __return_type__: type[MethodReturnType]

    def transform_response(
        self,
        raw_response: RawResponse,
        client: Client,
    ) -> MethodReturnType:
        if issubclass(self.__return_type__, BaseModel):
            return self.__return_type__.model_validate(
                raw_response.json,
                context={"client": client},
            )

        raise RuntimeError(
            f"{self.__class__.__name__}.return_type must return an subclass of BaseModel"
        )

    def get_request_body(self) -> dict[str, Any]:
        return self.model_dump(exclude_none=True, by_alias=True)

    async def execute(self, client: Client) -> MethodReturnType:
        response = await client.session.request(
            method=self,
        )
        return self.transform_response(response, client)

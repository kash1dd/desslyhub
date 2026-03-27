from __future__ import annotations

from http import HTTPMethod

from desslyhub.types.steam import SendSteamGiftGame
from desslyhub.methods.base import DesslyHubMethod


__all__ = ("SendSteamGiftGameMethod",)


class SendSteamGiftGameMethod(DesslyHubMethod[SendSteamGiftGame]):
    """
    Buying the game

    Source: https://desslyhub.readme.io/reference/post_apiv1steamgift
    """

    __api_method__: str = "v1/service/steamgift/sendgames"
    __http_method__: HTTPMethod = HTTPMethod.POST
    __return_type__: type[SendSteamGiftGame] = SendSteamGiftGame

    invite_url: str
    """Link for quickly adding a Steam user as a friend"""
    package_id: str
    """id of a specific game edition, obtained in Get Game By App ID for a specific game edition"""
    region: str
    """The recipient's region to which the game should be sent"""
    reference: str | None = None
    """your ID, if necessary"""

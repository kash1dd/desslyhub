from __future__ import annotations


class DesslyHubError(Exception):
    """
    Base class for all exceptions in the Dessly HUB API client.
    """


class DesslyHubAPIError(DesslyHubError):
    """
    Base class for API errors from Dessly HUB.
    """

    code: int
    message: str

    def __init__(self, message: str | None = None):
        self.message = message or self.__class__.message
        super().__init__(f"[{self.code}] {self.message}")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(code={self.code}, message={self.message})"


class InternalServerError(DesslyHubAPIError):
    code = -1
    message = "Internal server error"


class InsufficientFundsError(DesslyHubAPIError):
    code = -2
    message = "Insufficient funds in the balance"


class IncorrectAmountError(DesslyHubAPIError):
    code = -3
    message = "Incorrect amount"


class IncorrectRequestBodyError(DesslyHubAPIError):
    code = -4
    message = "Incorrect request body"


class AccessDeniedError(DesslyHubAPIError):
    code = -5
    message = "Access denied"


class InvalidTransactionIDError(DesslyHubAPIError):
    code = -151
    message = "Invalid transaction ID"


class TransactionNotFoundError(DesslyHubAPIError):
    code = -152
    message = "Transaction not found"


class PageNumberNotSpecifiedError(DesslyHubAPIError):
    code = -153
    message = "Page number not specified"


class InvalidFriendLinkError(DesslyHubAPIError):
    code = -51
    message = "Invalid link for adding friends"


class IncorrectAppIDError(DesslyHubAPIError):
    code = -52
    message = "Incorrect app ID"


class GameInfoNotFoundError(DesslyHubAPIError):
    code = -53
    message = "Information about the game not found"


class MainGameNotOwnedError(DesslyHubAPIError):
    code = -54
    message = "The user doesn't have the main game"


class GameAlreadyOwnedError(DesslyHubAPIError):
    code = -55
    message = "The user already has the game"


class UnableToAddFriendError(DesslyHubAPIError):
    code = -56
    message = "Unable to add as a friend"


class IncorrectCustomerRegionError(DesslyHubAPIError):
    code = -57
    message = "Incorrect customer region specified"


class RecipientRegionUnavailableError(DesslyHubAPIError):
    code = -58
    message = "The recipient's region is not available for gift"


class BotFriendActionPendingError(DesslyHubAPIError):
    code = -59
    message = "The user did not add/remove the bot from their friends list"


class IncorrectSteamUsernameError(DesslyHubAPIError):
    code = -100
    message = "Incorrect Steam username"


class IncorrectCurrencyValueError(DesslyHubAPIError):
    code = -120
    message = "Incorrect currency value"


class CurrencyNotSupportedError(DesslyHubAPIError):
    code = -121
    message = "Currency not supported"


class MobileGameNotFoundError(DesslyHubAPIError):
    code = -200
    message = "Mobile game not found"


class MobileGamePositionNotFoundError(DesslyHubAPIError):
    code = -201
    message = "Mobile game position not found"


class SourceVariantNotFoundError(DesslyHubAPIError):
    code = -202
    message = "Source variant not found"


class VoucherNotFoundError(DesslyHubAPIError):
    code = -300
    message = "Voucher not found"


class VoucherNotAvailableError(DesslyHubAPIError):
    code = -301
    message = "Voucher is not available"

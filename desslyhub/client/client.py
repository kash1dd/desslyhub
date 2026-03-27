from __future__ import annotations

from desslyhub.enums import Variant, Currency
from desslyhub.types import (
    Balance,
    BuyVoucher,
    SteamTopUp,
    Transaction,
    SteamGameList,
    MobileGameList,
    VoucherProduct,
    CheckSteamLogin,
    TransactionList,
    MobileGameRefill,
    MobileGameDetails,
    SendSteamGiftGame,
    SteamExchangeRate,
    TransactionStatus,
    SteamExchangeRates,
    VoucherProductList,
    SteamGameDetailsList,
)
from desslyhub.methods import (
    BuyVoucherMethod,
    GetBalanceMethod,
    SteamTopUpMethod,
    GetMobileGamesMethod,
    GetTransactionMethod,
    CheckSteamLoginMethod,
    GetTransactionsMethod,
    GetSteamGiftGamesMethod,
    GetVoucherProductMethod,
    SendSteamGiftGameMethod,
    GetVoucherProductsMethod,
    GetMobileGameDetailsMethod,
    GetSteamExchangeRateMethod,
    GetTransactionStatusMethod,
    SendMobileGameRefillMethod,
    GetSteamExchangeRatesMethod,
    GetSteamGiftGameDetailsMethod,
)
from desslyhub.client.session import BaseSession, AiohttpSession


__all__ = ("Client",)


class Client:
    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://desslyhub.com/api/",
        session: BaseSession | None = None,
    ) -> None:
        self._session: BaseSession = session or AiohttpSession(
            api_key=api_key,
            base_url=base_url,
        )

    @property
    def session(self) -> BaseSession:
        return self._session

    @property
    def api_key(self) -> str:
        return self._session.api_key

    @property
    def base_url(self) -> str:
        return self._session.base_url

    async def close(self) -> None:
        await self._session.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def get_balance(self) -> Balance:
        """
        Receiving a merchant balance

        Source: https://desslyhub.readme.io/reference/put_apiv1merchantsbalance

        :return: Balance object
        """

        method = GetBalanceMethod()
        return await method.execute(self)

    async def get_transaction(self, transaction_id: str) -> Transaction:
        """
        Retrieving a single transaction by id

        Source: https://desslyhub.readme.io/reference/get_apiv1transaction

        :param transaction_id: The id of the transaction to retrieve
        :return: Transaction object
        """

        method = GetTransactionMethod(transaction_id=transaction_id)
        return await method.execute(self)

    async def get_transaction_status(self, transaction_id: str) -> TransactionStatus:
        """
        Checking transaction status

        Source: https://desslyhub.readme.io/reference/get_apiv1statustransaction_id

        :param transaction_id: The id of the transaction to check
        :return: TransactionStatus object
        """

        method = GetTransactionStatusMethod(transaction_id=transaction_id)
        return await method.execute(self)

    async def get_transactions(self, page: int = 1) -> TransactionList:
        """
        Receiving all transactions page by page
        Transactions are returned page by page, starting with the most recent ones. 100 transactions per request. If the page number exceeds the number of your transactions, an empty list will be returned.

        Source: https://desslyhub.readme.io/reference/get_transactions

        :param page: Transaction page number. Counting starts from 1.
        :return: TransactionList object
        """  # noqa: E501

        method = GetTransactionsMethod(page=page)
        return await method.execute(self)

    async def check_steam_login(self, amount: float, username: str) -> CheckSteamLogin:
        """
        Check if a Steam account can be topped up.

        Source: https://desslyhub.readme.io/reference/post_apiv1servicesteamtopupcheck_login

        :param amount: Deposit amount in USD, ranging from 0.1 to 1000
        :param username: Steam user login
        :return: CheckSteamLogin object
        """

        method = CheckSteamLoginMethod(amount=amount, username=username)
        return await method.execute(self)

    async def steam_top_up(
        self,
        amount: float,
        username: str,
        reference: str | None = None,
    ) -> SteamTopUp:
        """
        Top up a Steam account.

        Source: https://desslyhub.readme.io/reference/post_apiv1servicesteamtopuptopup

        :param amount: Deposit amount in USD, ranging from 0.1 to 1000
        :param username: Steam user login
        :param reference: Your ID, if necessary
        :return: SteamTopUp object
        """

        method = SteamTopUpMethod(amount=amount, username=username, reference=reference)
        return await method.execute(self)

    async def get_steam_gift_games(self) -> SteamGameList:
        """
        Obtaining a list of games available for purchase

        Source: https://desslyhub.readme.io/reference/get_apiv1steamgames

        :return: SteamGameList object
        """

        method = GetSteamGiftGamesMethod()
        return await method.execute(self)

    async def get_steam_gift_game_details(self, app_id: int) -> SteamGameDetailsList:
        """
        Obtaining information about specific editions of the game by its app_id

        Source: https://desslyhub.readme.io/reference/get_apiv1steamgamesapp_id

        :param app_id: The app_id of the game to retrieve details for
        :return: SteamGameDetailsList object
        """

        method = GetSteamGiftGameDetailsMethod(app_id=app_id)
        return await method.execute(self)

    async def send_steam_gift_game(
        self,
        invite_url: str,
        package_id: str,
        region: str,
        reference: str | None = None,
    ) -> SendSteamGiftGame:
        """
        Buying the game

        Source: https://desslyhub.readme.io/reference/post_apiv1steamgift

        :param invite_url: Link for quickly adding a Steam user as a friend
        :param package_id: id of a specific game edition, obtained in Get Game By App ID for a specific game edition
        :param region: The recipient's region to which the game should be sent
        :param reference: your ID, if necessary
        :return: SendSteamGiftGame object
        """  # noqa: E501

        method = SendSteamGiftGameMethod(
            invite_url=invite_url,
            package_id=package_id,
            region=region,
            reference=reference,
        )
        return await method.execute(self)

    async def get_steam_exchange_rate(self, currency: Currency) -> SteamExchangeRate:
        """
        Obtaining the exchange rate for a specific currency.

        Source: https://desslyhub.readme.io/reference/get-exchange-rate

        :param currency: The currency code to get the exchange rate for
        :return: SteamExchangeRate object
        """

        method = GetSteamExchangeRateMethod(currency=currency.value)
        return await method.execute(self)

    async def get_steam_exchange_rates(self) -> SteamExchangeRates:
        """
        Obtaining exchange rates for all supported currencies.

        Source: https://desslyhub.readme.io/reference/get-all-exchange-rates

        :return: SteamExchangeRates object
        """

        method = GetSteamExchangeRatesMethod()
        return await method.execute(self)

    async def get_voucher_products(self) -> VoucherProductList:
        """
        Obtaining information about vouchers

        Source: https://desslyhub.readme.io/reference/get_voucher_products

        :return: VoucherProductList object
        """

        method = GetVoucherProductsMethod()
        return await method.execute(self)

    async def get_voucher_product(self, product_id: int) -> VoucherProduct:
        """
        Obtaining information about a specific voucher by its identifier

        Source: https://desslyhub.readme.io/reference/get_voucher_by_id

        :param product_id: The ID of the voucher product to retrieve
        :return: VoucherProduct object
        """

        method = GetVoucherProductMethod(product_id=product_id)
        return await method.execute(self)

    async def buy_voucher(
        self,
        root_id: int,
        variant_id: int,
        reference: str | None = None,
    ) -> BuyVoucher:
        """
        Purchasing a voucher

        Source: https://desslyhub.readme.io/reference/buy_voucher

        :param root_id: ID of a specific voucher obtained in Get Vouchers or Get Voucher By ID
        :param variant_id: ID of a specific variant obtained in Get Vouchers or Get Voucher By ID
        :param reference: your ID, if necessary
        :return: BuyVoucher object
        """

        method = BuyVoucherMethod(
            root_id=root_id,
            variant_id=variant_id,
            reference=reference,
        )
        return await method.execute(self)

    async def get_mobile_games(
        self,
        variant: Variant = Variant.PROVIDER_1,
    ) -> MobileGameList:
        """
        Obtaining a list of games available for replenishment, indicating the source option.

        Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgames

        :param variant: The source option for mobile games
        :return: MobileGameList object
        """

        method = GetMobileGamesMethod(variant=variant)
        return await method.execute(self)

    async def get_mobile_game_details(
        self,
        game_id: str,
        variant: Variant = Variant.PROVIDER_1,
    ) -> MobileGameDetails:
        """
        Obtaining information about a specific game by its identifier, indicating the source option.

        Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgamesid

        :param game_id: The id of the mobile game to retrieve details for
        :param variant: The source option for mobile games
        :return: MobileGameDetails object
        """  # noqa: E501

        method = GetMobileGameDetailsMethod(variant=variant, game_id=game_id)
        return await method.execute(self)

    async def send_mobile_game_refill(
        self,
        fields: dict[str, str],
        position: int,
        variant: Variant = Variant.PROVIDER_1,
        reference: str | None = None,
    ) -> MobileGameRefill:
        """
        Mobile game top-ups with a choice of payment source.

        Source: https://desslyhub.readme.io/reference/get_apiv1servicemobilevariantvariantgamesrefill

        :param fields: key-value data set specified when obtaining game information on the Get Game By ID handle
        :param position: ID of a specific position, obtained in Get Game By App ID for a specific game
        :param variant: The source option for mobile games
        :param reference: your ID, if necessary
        :return: MobileGameRefill object
        """  # noqa: E501

        method = SendMobileGameRefillMethod(
            variant=variant,
            fields=fields,
            position=position,
            reference=reference,
        )
        return await method.execute(self)

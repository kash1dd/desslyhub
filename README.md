# desslyhub

Асинхронная Python-библиотека для работы с [DesslyHub API](https://desslyhub.com). Поддерживает пополнение Steam-аккаунтов, покупку и отправку игр в подарок, ваучеры, пополнение мобильных игр и управление транзакциями.

## Установка

```bash
# Using uv
uv add desslyhub

# Or using pip
pip install desslyhub
```

**Требования:** Python 3.11+

## Быстрый старт

```python
import asyncio

from desslyhub import Client


async def main() -> None:
    async with Client(api_key="ваш_api_ключ") as client:
        balance = await client.get_balance()
        print(f"Баланс: {balance.balance} USD")


asyncio.run(main())
```

## Возможности

### Баланс и транзакции

```python
# Получить баланс
balance = await client.get_balance()

# Получить список транзакций (постранично, 100 на страницу)
transactions = await client.get_transactions(page=1)
for tx in transactions.transactions:
    print(f"{tx.id} — {tx.status} — {tx.final_amount} USD")

# Получить транзакцию по ID
transaction = await client.get_transaction("uuid-транзакции")

# Проверить статус транзакции
status = await client.get_transaction_status("uuid-транзакции")
print(status.status)  # success / pending / failed / cancelled
```

### Пополнение Steam

```python
# Проверить возможность пополнения аккаунта
check = await client.check_steam_login(amount=5.0, username="steam_login")
if check.can_refill:
    # Пополнить баланс Steam (от 0.1 до 1000 USD)
    result = await client.steam_top_up(amount=5.0, username="steam_login")
    print(f"Транзакция: {result.transaction_id}, статус: {result.status}")
```

### Покупка и отправка игр в подарок

```python
# Список доступных игр
games = await client.get_steam_gift_games()
for game in games.games:
    print(f"{game.name} (app_id: {game.app_id})")

# Детали игры: издания, регионы, цены
details = await client.get_steam_gift_game_details(app_id=730)
for edition in details.game:
    print(f"{edition.edition} (package_id: {edition.package_id})")
    for region in edition.regions_info:
        print(f"  {region.region}: {region.price} USD (скидка {region.discount}%)")

# Отправить игру в подарок
result = await client.send_steam_gift_game(
    invite_url="https://s.team/p/...",
    package_id="12345",
    region="RU",
)
```

### Курсы валют Steam

```python
from desslyhub.enums import Currency

# Курс для одной валюты
rate = await client.get_steam_exchange_rate(Currency.RUB)
print(f"1 USD = {rate.exchange_rate} RUB")

# Все курсы
rates = await client.get_steam_exchange_rates()
for currency, value in rates.exchange_rates.items():
    print(f"{currency.name}: {value}")
```

### Ваучеры

```python
# Список продуктов
products = await client.get_voucher_products()
for product in products.products:
    print(f"{product.name} ({product.country})")
    for v in product.variations:
        print(f"  {v.name} — {v.price} {v.voucher_currency} (в наличии: {v.stock})")

# Детали продукта
product = await client.get_voucher_product(product_id=1)

# Покупка ваучера
result = await client.buy_voucher(root_id=1, variant_id=10)
for voucher in result.vouchers:
    print(f"PIN: {voucher.pin}, S/N: {voucher.serial_number}")
```

### Мобильные игры

```python
from desslyhub.enums import Variant

# Список игр
games = await client.get_mobile_games(variant=Variant.PROVIDER_1)

# Детали игры (серверы, поля, позиции)
details = await client.get_mobile_game_details(game_id="123")
for pos in details.positions:
    print(f"{pos.name} — {pos.price} USD")

# Пополнение
result = await client.send_mobile_game_refill(
    fields={"user_id": "12345", "server": "EU"},
    position=1,
    variant=Variant.PROVIDER_1,
)
```

## Обработка ошибок

Библиотека предоставляет типизированные исключения для каждого кода ошибки API:

```python
from desslyhub.exceptions import (
    DesslyHubAPIError,
    InsufficientFundsError,
    IncorrectSteamUsernameError,
    GameAlreadyOwnedError,
)

try:
    await client.steam_top_up(amount=5.0, username="login")
except InsufficientFundsError:
    print("Недостаточно средств на балансе")
except IncorrectSteamUsernameError:
    print("Неверный логин Steam")
except DesslyHubAPIError as e:
    print(f"Ошибка API: код {e.code}, {e.message}")
```

<details>
<summary>Полный список исключений</summary>

| Код | Класс | Описание |
|-----|-------|----------|
| -1 | `InternalServerError` | Внутренняя ошибка сервера |
| -2 | `InsufficientFundsError` | Недостаточно средств |
| -3 | `IncorrectAmountError` | Некорректная сумма |
| -4 | `IncorrectRequestBodyError` | Некорректное тело запроса |
| -5 | `AccessDeniedError` | Доступ запрещён |
| -51 | `InvalidFriendLinkError` | Неверная ссылка на друга |
| -52 | `IncorrectAppIDError` | Неверный App ID |
| -53 | `GameInfoNotFoundError` | Информация об игре не найдена |
| -54 | `MainGameNotOwnedError` | Базовая игра не куплена |
| -55 | `GameAlreadyOwnedError` | Игра уже в библиотеке |
| -56 | `UnableToAddFriendError` | Не удалось добавить в друзья |
| -57 | `IncorrectCustomerRegionError` | Неверный регион покупателя |
| -58 | `RecipientRegionUnavailableError` | Регион получателя недоступен |
| -59 | `BotFriendActionPendingError` | Ожидается действие с ботом |
| -100 | `IncorrectSteamUsernameError` | Неверный логин Steam |
| -120 | `IncorrectCurrencyValueError` | Неверное значение валюты |
| -121 | `CurrencyNotSupportedError` | Валюта не поддерживается |
| -151 | `InvalidTransactionIDError` | Неверный ID транзакции |
| -152 | `TransactionNotFoundError` | Транзакция не найдена |
| -153 | `PageNumberNotSpecifiedError` | Не указан номер страницы |
| -200 | `MobileGameNotFoundError` | Мобильная игра не найдена |
| -201 | `MobileGamePositionNotFoundError` | Позиция не найдена |
| -202 | `SourceVariantNotFoundError` | Провайдер не найден |
| -300 | `VoucherNotFoundError` | Ваучер не найден |
| -301 | `VoucherNotAvailableError` | Ваучер недоступен |

</details>

## Поддерживаемые валюты

`Currency` — это `IntEnum` с 37 валютами:

USD, GBP, EUR, CHF, RUB, PLN, BRL, JPY, NOK, IDR, MYR, PHP, SGD, THB, VND, KRW, UAH, MXN, CAD, AUD, NZD, CNY, INR, CLP, PEN, COP, ZAR, HKD, TWD, SAR, AED, ILS, KZT, KWD, QAR, CRC, UYU
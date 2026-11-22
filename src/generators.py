from typing import Any, Iterator


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str
) -> Iterator[dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.
    Возвращает итератор, который выдает транзакции по одной.
    """
    for transaction in transactions:
        # Безопасно достаем код валюты из вложенного словаря
        transaction_currency = (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
        )
        if transaction_currency == currency:
            yield transaction


def transaction_descriptions(
    transactions: list[dict[str, Any]],
) -> Iterator[str]:
    """
    Возвращает описания (description) для каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX.
    Принимает начальное и конечное значение (включительно).
    """
    for number in range(start, stop + 1):
        # Превращаем число в строку и добиваем нулями до 16 символов
        card_number = str(number).zfill(16)
        # Форматируем с пробелами
        formatted_card = (
            f"{card_number[:4]} {card_number[4:8]} "
            f"{card_number[8:12]} {card_number[12:]}"
        )
        yield formatted_card

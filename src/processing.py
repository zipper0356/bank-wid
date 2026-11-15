from typing import Any

def filter_by_state(date: list[dict[str,Any]], state: str = "EXECUTED") ->list[dict[str, Any]]:
    """
    Фильтрует список словарей по ключу 'state'.

    :param date: Список словарей с данными о банковских операциях.
    :param state: Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.
    :return: Новый список словарей, содержащий только походящие записи.
    """
    return [item for item in date if item.get("state") == state]

def sort_by_date(date: list[dict[str,Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.

    :param date: Список словарей с данными о банковских операциях.
    :param reverse: Порядок сортировки. По умолчанию True (по убыванию).
    :return: Новый список словарей, отсортированный по дате.
    """

    return  sorted(date, key=lambda  x: x.get("date", ""), reverse=reverse)

from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(info_string: str) -> str:
    if not info_string or not info_string.strip():
        return "Ошибка: пустой ввод"

    parts = info_string.strip().split()
    if len(parts) < 2 or len(parts) > 5:
        return "Ошибка: некорректный формат ввода"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name or "счет" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"

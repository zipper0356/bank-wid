from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Фильтрует список словарей по ключу 'state'

    :param data: Список словарей с данными о банковских операциях.
    :param state: Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.
    :return: Новый список словарей, содержащий только подходящие записи.
    """
    return [item for item in data if
item.get("state") == state]


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    :param data: Список словарей с данными о банковских операциях.
    :param reverse: Порядок сортировки. По умолчанию True (по убыванию)
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(data, key=lambda x:
    x.get("date", ""), reverse=reverse)

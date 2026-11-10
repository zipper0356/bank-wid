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

    :param date: Список словарей  с данными о банковских операциях.
    :param reverse: Порядок сортировки. По умолчанию True (по убыванию).
    :return: Новый список словарей, отсортированный по дате.
    """

    return  sorted(date, key=lambda  x: x.get("date", ""), reverse=reverse)

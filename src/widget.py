from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета."""
    if not info_string or not info_string.strip():
        return "Ошибка: пустой ввод"

    parts = info_string.strip().split()

    if len(parts) < 2 or len(parts) > 5:
        return "Ошибка: некорректный формат ввода"

    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name or "счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """Преобразует дату из ISO-формата в ДД.ММ.ГГГГ."""
    try:
        dt = datetime.fromisoformat(date_string)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: некорректный формат даты"

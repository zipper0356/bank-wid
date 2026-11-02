from datetime import datetime


from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info_string: src) -> src:
    """Принимает строку с типом и номером карты/счета.
    Возвращает строку с замаскированным номером.
    """
    if info_string and info_string.strip():
        parts = info_string.strip().split()
        if 2 > len(parts) or len(parts) > 5:
            return "Ошибка: некоректный формат ввода"
        number = parts[-1]
        name = " ".join(parts[:-1])
        if "Счет" not in name and "счет" not in name:
            return f'{name} {get_mask_card_number(number)}'
        else:
            return f"{name}{get_mask_account(number)}"

    return "Ошибка: пустой ввод"


def get_date(date_string: str) -> str:
    """
    Принимает строку с датой в ISO-формате.
    Возвращает строку с датой в формате ДД.ММ.ГГГГ.
    """
    try:
        dt = (
datetime.fromisoformat(date_string))
        return dt.strftime("%d.%m.%y")
    except ValueError:
        return "Ошибка: некорректный формат даты"

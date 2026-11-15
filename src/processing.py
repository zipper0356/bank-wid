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

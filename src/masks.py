def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""

    if not card_number.isdigit() or len(card_number) != 16:
        return "Некорректный номер карты"

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета."""

    if not account_number.isdigit():
        return "Некорректный номер счета"

    return f"**{account_number[-4:]}"

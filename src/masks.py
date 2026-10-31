def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера карты в формате ХХХХ ХХ** **** ХХХХ."""
    clean_numbers = card_number.replace("", "")
    if len(clean_numbers) != 16:
        return "Ошибка: номер карты должен содердать 16 цифр"
    return f"{clean_numbers[:4]} {clean_numbers[4:6]}** ****{clean_numbers[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета в форме **ХХХХ."""
    if len(account_number) != 20:
        return "Ошибка:номер счета должен содержать 20 цифры"
    return f"**{account_number[-4:]}"

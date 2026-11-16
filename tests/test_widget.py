import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_mask_account_card(input_string, expected):
    """Тестирование маскировки карт и счетов."""
    assert mask_account_card(input_string) == expected


@pytest.mark.parametrize(
    "input_string",
    ["", "Счет", "Visa Platinum", "Visa Platinum 7000 7922 8960 6361 extra"],
)
def test_mask_account_card_invalid(input_string):
    """Проверка устойчивости к неверному вводу."""
    result = mask_account_card(input_string)
    assert "Ошибка" in result or "Некорректный" in result


def test_get_date():
    """Тестирование преобразования даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_invalid():
    """Проверка обработки неверной даты."""
    assert get_date("invalid-date") == "Некорректный формат даты"

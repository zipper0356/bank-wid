import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number_valid(card_number, expected):
    """Тестирование правильности маскирования карты."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number",
    ["1234", "70007922896063611234", "7000-7922-8960-6361", ""],
)
def test_get_mask_card_number_invalid(card_number):
    """Проверка обработки неверных форматов номеров карт."""
    assert get_mask_card_number(card_number) == "Некорректный номер карты"


def test_get_mask_account_valid():
    """Тестирование правильности маскирования счета."""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234") == "**1234"


def test_get_mask_account_invalid():
    """Проверка обработки неверных счетов."""
    assert get_mask_account("abc") == "Некорректный номер счета"

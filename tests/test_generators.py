import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD", "name": "US Dollar"}},
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "RUB", "name": "Ruble"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD", "name": "US Dollar"}},
            "description": "Перевод с карты на карту",
        },
        {},  # Транзакция без данных
    ]


def test_filter_by_currency_usd(sample_transactions):
    """Тест фильтрации по валюте USD."""
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert len(result) == 2
    # Чтобы не было длинной строки, используем цикл
    for tx in result:
        code = tx["operationAmount"]["currency"]["code"]
        assert code == "USD"


def test_filter_by_currency_empty_result(sample_transactions):
    """Тест, когда нет транзакций с нужной валютой."""
    gen = filter_by_currency(sample_transactions, "EUR")
    assert list(gen) == []


def test_transaction_descriptions(sample_transactions):
    """Тест генератора описаний."""
    gen = transaction_descriptions(sample_transactions)
    result = list(gen)
    assert len(result) == 4
    assert result[0] == "Перевод организации"
    assert result[3] == ""  # Для пустого словаря


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",

                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Параметризованный тест генератора номеров карт."""
    gen = card_number_generator(start, stop)
    assert list(gen) == expected

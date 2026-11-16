import pytest


@pytest.fixture
def sample_operations():
    """Фикстура с тестовыми данными операций."""
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-15T14:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-12-31T23:59:59"},
        # Одинаковая дата для проверки сортировки
        {"id": 4, "state": "PENDING", "date": "2023-01-01T10:00:00"},
    ]

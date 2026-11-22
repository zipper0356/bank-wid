import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(sample_operations):
    """Тестирование фильтрации по статусу EXECUTED (по умолчанию)."""
    result = filter_by_state(sample_operations)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize("state", ["CANCELED", "PENDING", "UNKNOWN"])
def test_filter_by_state_custom(sample_operations, state):
    """Параметризация тестов для разных статусов."""
    result = filter_by_state(sample_operations, state)
    if state == "UNKNOWN":
        assert len(result) == 0
    else:
        assert all(op["state"] == state for op in result)


def test_sort_by_date_descending(sample_operations):
    """Тестирование сортировки по убыванию (по умолчанию)."""
    result = sort_by_date(sample_operations)
    assert result[0]["id"] == 2  # 2023-05-15 - самая поздняя
    assert result[-1]["id"] == 3  # 2022-12-31 - самая ранняя


def test_sort_by_date_ascending(sample_operations):
    """Тестирование сортировки по возрастанию."""
    result = sort_by_date(sample_operations, reverse=False)
    assert result[0]["id"] == 3  # 2022-12-31
    assert result[-1]["id"] == 2  # 2023-05-15

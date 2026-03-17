import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-01T12:00:00"},
    ]


def test_filter_by_state_executed(transactions):
    """Проверка фильтрации EXECUTED (по умолчанию)"""
    result = filter_by_state(transactions)
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_filter_by_state_canceled(transactions):
    """Проверка фильтрации CANCELED"""
    result = filter_by_state(transactions, state="CANCELED")
    assert len(result) == 1
    assert result[0]["id"] == 2


def test_filter_by_state_empty(transactions):
    """Проверка фильтрации несуществующего статуса"""
    result = filter_by_state(transactions, state="PENDING")
    assert result == []


def test_sort_by_date_desc(transactions):
    """Сортировка от новых к старым (по умолчанию)"""
    result = sort_by_date(transactions)
    assert result[0]["id"] == 2  # 2024 год
    assert result[2]["id"] == 3  # 2022 год


def test_sort_by_date_asc(transactions):
    """Сортировка от старых к новым (reverse=False)"""
    result = sort_by_date(transactions, reverse=False)
    assert result[0]["id"] == 3  # 2022 год


def test_sort_by_date_no_date():
    """Сортировка, если дата отсутствует"""
    data = [{"id": 1}, {"id": 2, "date": "2023-01-01"}]
    result = sort_by_date(data)
    assert len(result) == 2
    assert result[0]["id"] == 2


def test_filter_empty_list():
    """Тест фильтрации пустого списка (строка с return)"""
    assert filter_by_state([], "EXECUTED") == []


def test_filter_no_state_key():
    """Тест случая, когда в словаре нет ключа 'state'"""
    data = [{"id": 1}, {"state": "EXECUTED", "id": 2}]
    # .get() вернет None, и элемент с id: 1 не попадет в список
    assert filter_by_state(data) == [{"state": "EXECUTED", "id": 2}]


def test_sort_empty_list():
    """Тест сортировки пустого списка"""
    assert sort_by_date([]) == []


def test_sort_by_date_ascending():
    """Тест сортировки по возрастанию (проверка параметра reverse=False)"""
    data = [{"date": "2019-01-01"}, {"date": "2020-01-01"}]
    result = sort_by_date(data, reverse=False)
    assert result[0]["date"] == "2019-01-01"

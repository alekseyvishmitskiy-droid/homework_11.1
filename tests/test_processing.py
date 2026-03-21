import pytest

from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_card_and_account


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Maestro 1596837814705307", "Maestro 1596 83** **** 5307"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Ошибка: Пустая строка"),
    ],
)
def test_mask_card_and_account_valid(input_string, expected):
    """Проверка маскировки корректных данных карт и счетов"""
    assert mask_card_and_account(input_string) == expected


def test_mask_card_and_account_invalid_number():
    """Проверка обработки ошибки при некорректном номере (например, коротком)"""
    result = mask_card_and_account("Visa 123")
    assert "Ошибка:" in result


@pytest.mark.parametrize(
    "date_input, expected_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-12-31T23:59:59", "31.12.2018"),
    ],
)
def test_get_date_valid(date_input, expected_date):
    """Проверка правильного форматирования даты"""
    assert get_date(date_input) == expected_date


def test_get_date_invalid_format():
    """Проверка реакции на неверный формат строки даты"""
    assert get_date("неправильная-дата") == "Ошибка: Неверный формат входных данных"


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-02-01T12:00:00"},
    ]


def test_filter_by_state(sample_data):
    """Проверка фильтрации по статусу"""
    result = filter_by_state(sample_data, "EXECUTED")
    assert len(result) == 2  # подставьте актуальное число из ваших данных
    assert all(item["state"] == "EXECUTED" for item in result)


def test_sort_by_date(sample_data):
    """Проверка сортировки по дате"""
    result = sort_by_date(sample_data)
    assert result[0]["date"] > result[-1]["date"]

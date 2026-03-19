import pytest
from src.widget import mask_card_and_account, get_date


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

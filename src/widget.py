from src.masks import get_mask_account, get_mask_card_number

"""В модуле widget создайте функцию mask_account_card,
которая умеет обрабатывать информацию как о картах, так и о счетах.
Функция должна:

Принимать один аргумент — строку, содержащую тип и номер карты или счета.
Аргументом может быть строка типа
Visa Platinum 7000792289606361, или Maestro 7000792289606361,
 или Счет 73654108430135874305.
Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!

Возвращать строку с замаскированным номером.
Для карт и счетов используйте разные типы маскировки.
Переиспользуйте уже существующие функции маскировки из вашего проекта,
 чтобы избежать дублирования кода
"""

"""
В том же модуле создайте функцию get_date,
которая принимает на вход строку с датой в формате
"2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
"ДД.ММ.ГГГГ" ("11.03.2024").
"""


def mask_card_and_account(data: str) -> str:
    """Преобразуем счет и номер карты в зашифрованные данные"""
    try:
        parts = data.split()
        if not parts:
            return "Ошибка: Пустая строка"

        name = " ".join(parts[:-1])
        number = parts[-1]

        if "Счет" in name:
            masked_number = get_mask_account(number)
        else:
            masked_number = get_mask_card_number(number)

        return f"{name} {masked_number}"

    except ValueError as e:
        return f"Ошибка: {e}"


def get_date(date_string: str) -> str:
    """Преобразует дату в ДД.ММ.ГГГГ."""
    try:
        date_part = date_string.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except IndexError:
        return "Ошибка: Неверный формат входных данных"


if __name__ == "__main__":
    """Запрашиваем данные у пользователя"""
    card_info = input("Введите данные карты или счета: ")
    print(mask_card_and_account(card_info))

    date_info = input("Введите дату: ")
    print(get_date(date_info))

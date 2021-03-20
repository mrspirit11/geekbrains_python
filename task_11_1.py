# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

from datetime import date

class Date:
    _date: str
    @classmethod
    def __init__(cls, dmy: str) -> None:
        cls._date = dmy

    @classmethod
    def str_to_dmy(cls) -> map:
        return map(int, cls._date.split('-'))

    @staticmethod
    def date_validation(d: int, m: int, y: int) -> date:
        try:
            return date(y, m, d)
        except ValueError as e:
            print(e)


d1 = Date('1-12-2020')
# print(*d1.str_to_dmy())
print(Date.date_validation(*d1.str_to_dmy()))
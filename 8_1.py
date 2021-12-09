__author__ = 'Сафиулин Салават Тельманович'


# Задача-1: Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, data_text):
        self.data_day, self.data_month, self.data_year = Data.str_to_int(data_text)

    @classmethod
    def str_to_int(cls, data_text):
        day, month, year = data_text.split('-')
        return Data.valid(int(day), int(month), int(year))  # на ValueError не проверяю, проверка корректности цифр даты

    @staticmethod
    def valid(day, month, year):
        if day < 1 or day > 31:
            print('У даты введен некорректный день')
        elif month < 1 or month > 12:
            print('У даты введен некорректный месяц')
        elif year < 1:
            print('У даты введен некорректный год')
        return day, month, year  # Данные отдаем какие взяли, метод просто выводит сообщение о корректности данных


data1 = Data('2 - 11- 1122')
d, m, y = data1.str_to_int('0 - 11- 1111')
print(f"{d}, {m}, {y}")
print(f"{data1.data_day}, {data1.data_month}, {data1.data_year}")

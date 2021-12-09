__author__ = 'Сафиулин Салават Тельманович'


# Задача-7: Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'{self.a} + {self.b}*i'


a1 = ComplexNumber(2, 3)
a2 = ComplexNumber(2, 3)
a3 = ComplexNumber(2, 3)
print(a1)
print(a1 + a2 + a3)
print(a1 * a2 * a3)

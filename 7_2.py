__author__ = 'Сафиулин Салават Тельманович'

# Задача-2: Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def square_coat(self):
        pass

    @abstractmethod
    def square_costume(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def square_coat(self):
        return self.v / 6.5 + 0.5

    @property
    def square_costume(self):
        return 0


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def square_coat(self):
        return 0

    @property
    def square_costume(self):
        return 2 * self.h + 0.3


coat1 = Coat(6.5)
costume1 = Costume(5)
print(coat1.square_coat)
print(costume1.square_costume)
print('Общий расход ткани', coat1.square_coat + costume1.square_costume)

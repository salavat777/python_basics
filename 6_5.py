# Задача-5: Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery():
    title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        Stationery.title = 'pen'

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self):
        Stationery.title = 'pencil'

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def __init__(self):
        Stationery.title = 'handle'

    def draw(self):
        print('Запуск отрисовки маркером')


obj1 = Stationery()
obj1.draw()

obj2 = Pen()
obj2.draw()
print(obj2.title)

obj3 = Pencil()
obj3.draw()
print(obj3.title)

obj4 = Handle()
obj4.draw()
print(obj4.title)

obj5 = Pen()
obj5.draw()
print(obj5.title)

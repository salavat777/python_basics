# Задача-4: Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car():
    name = 'car'
    color = 'blanc'
    speed = 30
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print('go-go')

    def stop(self):
        print('stop car')

    def turn(self, direction):
        print(f'turn {direction}')

    def show_speed(self):
        print(f'current speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'current speed towncar {self.speed}')
        if self.speed > 60:
            print('WARNING!!! speed towncar is HI')


class WorkCar(Car):
    def show_speed(self):
        print(f'current speed workcar {self.speed}')
        if self.speed > 40:
            print('WARNING!!! speed workcar is HI')


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        Car.is_police = True
        Car.speed = speed


toyota = Car(50, 'blanc', 'toyota', False)
toyota.go()
toyota.turn('left')
toyota.stop()
toyota.show_speed()
ford = PoliceCar(80, 'blanc', 'toyota', False)
ford.show_speed()
print(ford.is_police)
bus = TownCar(80, 'blanc', 'toyota', False)
bus.show_speed()

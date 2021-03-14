# 4. Реализуйте базовый класс Car.

# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed: float, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self): 
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction): 
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car): 
    speed_limit = 60
    def show_speed(self):
        if self.speed > self.speed_limit:
            # \033[31m Форматирование цвета текста (31 Красный) на Windows < 10 не работает
            print(f'\033[31m Превышение скорости на {self.speed - self.speed_limit} \033[37m')
        else:
            super().show_speed()


class SportCar(Car): pass

class WorkCar(TownCar): 
    speed_limit = 40


class PoliceCar(Car): pass

garage = [Car(100, 'Red', 'Opel', False),
         TownCar(60, 'Red', 'BMW', False),
         SportCar(100, 'Red', 'AUDI', False),
         WorkCar(100, 'Red', 'MAN', False),
         PoliceCar(100, 'Red', 'Skoda', True)]


for car in garage:
    print('*'*10, car.__class__.__name__, '*'*10)
    print(car.name)
    car.go()
    car.stop()
    car.turn('left')
    car.show_speed()
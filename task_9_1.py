# 1. Создать класс TrafficLight (светофор).

# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
import time
class TrafficLight:

    _color_time = {'красный': 7, 
                   'жёлтый': 2, 
                   'зелёный': 5}

    def __init__(self, color):
        self.__color = color

    def running(self): 
        # while True:
        for i in range(10):
            print(self.__color)
            time.sleep(self._color_time[self.__color])
            # Find and save next color from _color_time
            self.__color = list(self._color_time)[
                (list(self._color_time).index(self.__color) + 1) % 3]


a = TrafficLight('зелёный')
a.running()

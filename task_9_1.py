# 1. Создать класс TrafficLight (светофор).

# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

# Насчет светофора. Цвета светофора - атрибут класса (очевидно), а вот тайминги задержек? Это ведь атрибут экземпляра. Но в коде running удобно иметь это одной структурой.
import time
# class TrafficLight:

#     _color_time = {'красный': 7, 
#                    'жёлтый': 2, 
#                    'зелёный': 5}

#     def __init__(self, color):
#         self.__color = color

#     def running(self): 
#         # while True:
#         for i in range(10):
#             print(self.__color)
#             time.sleep(self._color_time[self.__color])
#             # Find and save next color from _color_time
#             self.__color = list(self._color_time)[
#                 (list(self._color_time).index(self.__color) + 1) % 3]

class TrafficLight:

    _color = ('красный', 'жёлтый', 'зелёный')
    _default_color_time = {'жёлтый': 2, 'красный': 7, 'зелёный': 5}

    def running(self, color, color_time: dict, infinitely=False): 
        if not color_time:
            color_time = self._default_color_time
        i = 0
        while True:
            if infinitely is False:
                if i == len(self._color) + 1:
                    break
                i += 1
            print(color)
            time.sleep(color_time[color])
            # Find and save next color from _color
            color = self._color[
                (self._color.index(color) + 1) % 3]


a = TrafficLight()
a.running('зелёный', {'жёлтый': 2, 'красный': 7, 'зелёный': 5})

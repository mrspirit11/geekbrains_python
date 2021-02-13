# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах. Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек
# Примечание: можете проверить себя здесь: https://www.epochconverter.com/



# import random

# Для тестирования раскомментировать код

durations = [53, 153, 4153, 400153]
# durations = [random.randint(0,100000) for i in range(10)]

for duration in durations:
    # print(duration, end=' = ')
    s = duration % 60
    m = duration // 60 % 60
    h = duration // 3600 % 24
    d = duration // (24 * 3600)
    if d:
        print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
    elif h:
        print(h, 'час', m, 'мин', s, 'сек')
    elif m:
        print(m, 'мин', s, 'сек')
    else:
        print(s, 'сек')

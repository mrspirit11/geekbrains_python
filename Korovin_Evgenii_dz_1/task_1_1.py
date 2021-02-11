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

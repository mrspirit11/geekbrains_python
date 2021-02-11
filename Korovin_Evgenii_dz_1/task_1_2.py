list_of_cubes = [_ ** 3 for _ in range(1, 1000) if _ % 2]
for i in list_of_cubes:
    x = i
    numb_sum = 0
    while i > 0:
        numb_sum += i % 10
        i = i // 10
    if not numb_sum % 7:
        print('число:', x, 'sum:', numb_sum)

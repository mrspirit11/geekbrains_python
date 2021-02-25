# Практическое задание
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# |||
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#
# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(num: int):
    for el in range(1, num + 1, 2):
        yield el


n = 15
next_i = (lambda x: next(x) for _ in range(n+1))

# odd_to_15 = odd_nums(n)
# print(type(odd_to_15))
# for i in next_i:
#     print(i(odd_to_15))

odd_nums_adv = (i for i in range(1, n + 1, 2))
odd_to_15 = odd_nums_adv
print(type(odd_to_15))
for i in next_i:
    print(i(odd_to_15))


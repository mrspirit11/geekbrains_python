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


odd_to_15 = odd_nums(15)
print(type(odd_to_15))
for i in odd_to_15:
    print(i, end=',')
print()
# <class 'generator'>
# 1,3,5,7,9,11,13,15,

n = 15
odd_nums_adv = (i for i in range(1, n + 1, 2))
odd_to_15 = odd_nums_adv
print(type(odd_to_15))
for i in odd_to_15:
    print(i, end=',')
# <class 'generator'>
# 1,3,5,7,9,11,13,15,

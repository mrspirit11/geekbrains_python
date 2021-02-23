# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
#
#
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]


def list_of_max(li):
    uniqu = []
    tmp = set()
    for el in li:
        if el not in uniqu:
            uniqu.append(el)
        else:
            uniqu.remove(el)
        tmp.add(el)
    return uniqu


print(list(list_of_max(src)))

print([i for i in src if src.count(i) == 1])

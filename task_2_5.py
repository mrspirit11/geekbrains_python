# Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
#
# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


price_list = [78.26, 20.33, 71.89, 2.9, 40.02, 57.19, 67.02, 88.47, 59.24, 67.89, 52.37, 58.09, 41.65, 50.69, 6.69, 33, 49, 87.19, 33.15, 29.64]

string = ''
for _id, price in enumerate(price_list):
    if _id != 0:
        string += ', '
    string += f'{int(price)} руб {int(round(price%1, 2)*100):0>2d} коп'

print(string)

print(id(price_list))
price_list.sort()
print(id(price_list))
print(price_list)

sorted_price_list = sorted(price_list, reverse=True)
print(sorted_price_list)
print(sorted_price_list[:5])

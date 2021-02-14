# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
#
#
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам? Можно ли использовать словарь в этом случае?
# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам?
from pprint import pprint as pp


def thesaurus(*args: str) -> dict:
    return {name[0]: list(filter(lambda x: x[0] == name[0],
                                 args)) for name in args}


def thesaurus_adv(*args: str) -> dict:
    _by_surname = {name.split()[1][0]: {} for name in args}
    for i in args:
        f_surname = i.split()[1][0]
        f_name = i.split()[0][0]
        _by_names = {f_name: list(filter(lambda x: x.split()[0][0] == f_name and f_surname == x.split()[1][0], args))}
        _by_surname[f_surname].update(_by_names)
    return _by_surname


by_names = thesaurus("Иван", "Мария", "Петр", "Илья")
# Реверс в сортировке сделал для наглядности
by_names_sorted = dict(sorted(by_names.items(), key=lambda x: x[0].lower(), reverse=True))
by_surname = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(by_names, by_names_sorted, sep='\n\n', end='\n\n')
pp(by_surname)

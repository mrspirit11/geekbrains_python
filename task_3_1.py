# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.


# *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы - результат тоже должен быть с заглавной.
# Например:

# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# Словарь вынес за пределы функции, так как мне кажется, что так будет проще его исправлять/расширять,
# в идеале его бы вообще в отдельный модуль/файл/БД запихнуть (тогда его по хорошему передавать в параметры функции)

DICTIONARY = {'ноль': 'zero',
              'один': 'one',
              'два': 'two',
              'три': 'three',
              'четыре': 'four',
              'пять': 'five',
              'шесть': 'six',
              'семь': 'seven',
              'восемь': 'eight',
              'девять': 'nine',
              'десять': 'ten',
              'одиннадцать': 'eleven',
              'двенадцать': 'twelve'}


def num_translate_adv(word: str) -> str:
    word_translate_from_ru = DICTIONARY
    word_translate_from_en = {b: a for a, b in DICTIONARY.items()}

    if str(word).lower() in word_translate_from_ru:
        return word_translate_from_ru.get(word) if word.islower() else word_translate_from_ru.get(word.lower()).title()
    elif str(word).lower() in word_translate_from_en:
        return word_translate_from_en.get(word) if word.islower() else word_translate_from_en.get(word.lower()).title()
    # else:
    #     return 'Данного слова нет в словаре:('


test_list = ('один', 'Один', 'One',
             'one', '1', 'ДВА', 'дЕСЯТЬ',
             'TEN', 'six', 'sIX', 99, [1, 2, 3])

for w in test_list:
    print(w, num_translate_adv(w), sep=' = ')

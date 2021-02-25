# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         	Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?


from random import shuffle, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(numb_of_jokes=1, no_repeat=False):
    if no_repeat:
        list(map(shuffle, [nouns, adverbs, adjectives]))
        min_list_len = min(map(len, [nouns, adverbs, adjectives]))
        return [f"{nouns.pop()} {adverbs.pop()} {adjectives.pop()}" for _ in range(min_list_len)]
    else:
        return [' '.join(choice(list(zip(nouns, adverbs, adjectives)))) for _ in range(numb_of_jokes)]


print(get_jokes(10, no_repeat=True))

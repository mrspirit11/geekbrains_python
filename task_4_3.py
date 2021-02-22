# 2.	Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (USD, EUR, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу? Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
#
# 3.	*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

# 5.	*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

from datetime import datetime
import requests

URL = 'http://www.cbr.ru/scripts/XML_daily.asp'


def currency_rates(currency_code: str, url=URL) -> (datetime, float):
    def str_to_dict(text: str) -> dict:
        char_name = text[text.find('CharCode>'):text.find('</CharCode>')].split('>')
        out_dict = {char_name[1]: {}}
        str_to_find = (('Nominal>', '</Nominal>'),
                       ('Value>', '</Value>'))
        for start_str, end_str in str_to_find:
            _str = text[text.find(start_str):text.find(end_str)].split('>')
            if 'Val' in start_str:
                _str[1] = float(_str[1].replace(',', '.'))
            out_dict[char_name[1]][_str[0]] = _str[1]
        out_dict[char_name[1]]['V/N'] = out_dict[char_name[1]]['Value'] / float(out_dict[char_name[1]]['Nominal'])
        return out_dict

    response = requests.get(url).text
    valute_info = {}
    _date = response[response.find('Date='):response.find('name')].strip().split('=')
    valute_info[_date[0]] = datetime.strptime(_date[1], '"%d.%m.%Y"').date()
    for s in response.split('</Valute>'):
        if 'Valute' in s:
            valute_info.update(str_to_dict(s))
    return valute_info['Date'], valute_info[currency_code.upper()]['V/N'] if valute_info.get(
        currency_code.upper()) else None


if __name__ == "__main__":
    import sys
    # test 4_2-4_3
    # CURRENCY_CODES = ['USD', 'EUR', 'q', 'AMD']
    # for cur in CURRENCY_CODES:
    #     print(currency_rates(cur))

    # (datetime.date(2021, 2, 21), 73.9833)
    # (datetime.date(2021, 2, 21), 89.6604)
    # (datetime.date(2021, 2, 21), None)
    # (datetime.date(2021, 2, 21), 0.14106)

    # task 4_5
    for param in sys.argv[1:]:
        date, value = currency_rates(param)
        date = date.strftime("%d.%m.%Y")
        print(f'{value:.2f}', date, sep=', ')

    # python3 task_4_3.py USD EUR AMD
    # USD, 73.98, 21.02.2021
    # EUR, 89.66, 21.02.2021
    # AMD, 0.14, 21.02.2021

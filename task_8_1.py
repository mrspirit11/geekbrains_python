# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru


# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в данном случае использовать функцию re.compile()?
# *(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')


# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re


def email_parse(s_str: str) -> dict:
    email_regex = re.match(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)', s_str)
    if email_regex:
        return email_regex.groupdict()
    else:
        raise ValueError(f'wrong email: {s_str}')


def log_parse(file_path: str) -> list:
    try:
        log_regex = re.compile(r'(\b[\w\.:]+\b).+(?:\[(.+)\]) "(\w+) ((?:/\w+){2,}).+" (\d+) (\d+)')
        with open(file_path) as f_in:
            out_list = []
            for f_str in f_in:
                out_list.extend(log_regex.findall(f_str))
        return out_list
    except FileNotFoundError as e:
        print(f'file error {e.filename}')


if __name__ == '__main__':
    # print(email_parse('mrspirit11@gmail.com'))
    print(log_parse('nginx_logs.txt'))

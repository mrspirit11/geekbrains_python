# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
import re

from requests import get, codes
import os
import sys

def get_file(url: str, make_dir=True) -> str:
    """Download file from url. Return path to downloaded file.
    Params: url address,
            make_dir=True (make dir 'Download' in project directory"""
    path = ''
    if make_dir:
        path = 'Download'
        if path not in os.listdir():
            os.makedirs(path)
    response = get(url)
    if response.status_code == codes.ok:
        file_path = os.path.join(path, url.split('/')[-1] + '.txt')
        # проверка наличия файла и сравнение файлов по размеру (недостаток все равно нужно скачать инфу)
        if os.path.isfile(file_path) and abs(os.path.getsize(file_path)-sys.getsizeof(response.content)) < 50:
            print(f'{file_path} already in folder, skip download.')
        # Проверка наличия и размера файла
        # if os.path.isfile(file_path) and os.path.getsize(file_path):
        #     print(f'{file_path} already in folder, skip download.')

        else:
            with open(file_path, 'wb') as f_out:
                f_out.write(response.content)
            print(f'Success! File download to {file_path}')
        return file_path
    else:
        print(f'ERROR: response status code {response.status_code}')


def read_logs_file(path_to_file):
    with open(path_to_file) as f_in:
        return [(lambda x: (x[0], re.search(r'\w+', x[5])[0], x[6]))(line.split()) for line in f_in]


if __name__ == '__main__':
    URL = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
    file = get_file(URL)
    print(read_logs_file(file)[0])
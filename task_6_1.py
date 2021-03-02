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


import os, re
from requests import get, codes


def download_file(url: str, make_dir=True) -> str:
    """Download file from url. Return path to downloaded file.
    Params: url address,
            make_dir=True (make dir 'Download' in project directory"""
    path = ''
    if make_dir:
        path = 'Download'
        if path not in os.listdir():
            os.makedirs(path)
    file_path = os.path.join(path, url.split('/')[-1] + '.txt')
    if os.path.exists(file_path) and os.path.getsize(file_path):
        print(f'{file_path} already in folder, skip download.')
        return file_path
    else:
        response = get(url)
        if response.status_code == codes.ok:
            with open(file_path, 'wb') as f_out:
                f_out.write(response.content)
            print(f'Success! File download to {file_path}')
            return file_path
        else:
            print(f'ERROR: response status code {response.status_code}')


def read_logs_file(path_to_file: str, regex=False) -> list:

    def parse_list(s_list: list) -> tuple:
        return s_list[0], s_list[5][1:], s_list[6]

    def regex_search(s_line: str) -> tuple:
        ip = re.search(r'[\d.]+', s_line)[0]
        request = re.search(r'[A-Z]{2,}', s_line)[0]
        url = re.findall(r' (/\w+/\w+)', s_line)[0]
        return ip, request, url

    with open(path_to_file, encoding='UTF-8') as f_in:
        if regex:
            return [regex_search(line) for line in f_in]
        else:
            return [parse_list(line.split()) for line in f_in]


def find_spammer(s_list: list) -> list:
    out_dict = {}
    for i in s_list:
        out_dict.setdefault(i[0], 0)
        out_dict[i[0]] += 1
    max_requests_ip = sorted(out_dict, key=lambda x: out_dict[x], reverse=True)
    return [(ip, out_dict[ip]) for ip in max_requests_ip[:10]]


if __name__ == '__main__':
    from pprint import pprint as pp
    from time import perf_counter

    start = perf_counter()
    URL = 'https://github.com/elastic/examples/raw/master/\
Common%20Data%20Formats/nginx_logs/nginx_logs'
    file = download_file(URL)
    if file:
        from_file = read_logs_file('Download/nginx_logs.txt', regex=False)
        spammer = find_spammer(from_file)

        print('Подозрительные запросы:')
        pp(spammer)
        print('Логи')
        pp(from_file[:5])
        print(f'время{start-perf_counter()}')

# File download
# Success! File download to Download/nginx_logs.txt
# Подозрительные запросы:
# [('216.46.173.126', 2350),
#  ('180.179.174.219', 1720),
#  ('204.77.168.241', 1439),
#  ('65.39.197.164', 1365),
#  ('80.91.33.133', 1202),
#  ('84.208.15.12', 1120),
#  ('74.125.60.158', 1084),
#  ('119.252.76.162', 1064),
#  ('79.136.114.202', 628),
#  ('54.207.57.55', 532)]
# Логи
# [('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('80.91.33.133', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_2')]
# время-1.20943784


# File in folder
# Download/nginx_logs.txt already in folder, skip download.
# Подозрительные запросы:
# [('216.46.173.126', 2350),
#  ('180.179.174.219', 1720),
#  ('204.77.168.241', 1439),
#  ('65.39.197.164', 1365),
#  ('80.91.33.133', 1202),
#  ('84.208.15.12', 1120),
#  ('74.125.60.158', 1084),
#  ('119.252.76.162', 1064),
#  ('79.136.114.202', 628),
#  ('54.207.57.55', 532)]
# Логи
# [('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('80.91.33.133', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_2')]
# время-0.17098113900000006


# Regex search
# Download/nginx_logs.txt already in folder, skip download.
# Подозрительные запросы:
# [('216.46.173.126', 2350),
#  ('180.179.174.219', 1720),
#  ('204.77.168.241', 1439),
#  ('65.39.197.164', 1365),
#  ('80.91.33.133', 1202),
#  ('84.208.15.12', 1120),
#  ('74.125.60.158', 1084),
#  ('119.252.76.162', 1064),
#  ('79.136.114.202', 628),
#  ('54.207.57.55', 532)]
# Логи
# [('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('93.180.71.3', 'GET', '/downloads/product_1'),
#  ('80.91.33.133', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_1'),
#  ('217.168.17.5', 'GET', '/downloads/product_2')]
# время-0.448032427
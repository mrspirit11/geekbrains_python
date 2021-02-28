# -*- coding: utf8 -*-
# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
#
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, то для оставшихся ФИО значение в словаре - None.
# Если наоборот — формируем словарь, исходя из количества ФИО и выходим из скрипта с кодом «1». Примечание: При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
#
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
#
# скалолазание,охота
# горные лыжи

import json


def join_files(file1: str, file2: str):
    with open(file1) as f_in:
        file1_text = [line.strip().replace(',', ' ') for line in f_in]
    with open(file2) as f_in:
        file2_text = [line.strip() for line in f_in]
    with open('save_file.json', 'w') as f_out:
        if len(file2_text) < len(file1_text):
            json.dump({file1_text[i]: file2_text[i] if i < len(file2_text) else None
                        for i in range(len(file1_text))}, f_out)
        else:
            json.dump({file1_text[i]: file2_text[i] for i in range(len(file1_text))}, f_out)
            return 1


if __name__ == '__main__':
    print(join_files('users.csv', 'hobby.csv'))
    with open('save_file.json') as f_in:
        print(json.load(f_in))

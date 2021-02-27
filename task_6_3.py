# -*- coding: utf8 -*-
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
#
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи
#
# *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи
#
#
# **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

from os import path
import json


def join_files(file1, file2, file_name, dict_to_file=False):
    with open(file1) as f_in:
        file1_text = [line.strip().replace(',', ' ') for line in f_in]
    with open(file2) as f_in:
        file2_text = [line.strip() for line in f_in]
    if dict_to_file:
        with open(file_name, 'w') as f_out:
            json.dump({file1_text[i]: file2_text[i] if i < len(file2_text) else None
                       for i in range(len(file1_text))}, f_out)
    else:
        with open(file_name, 'w') as f_out:
            f_out.writelines((f'{file1_text[i]}: {file2_text[i] if i < len(file2_text) else None}\n'
                              for i in range(len(file1_text))))


if __name__ == '__main__':
    import sys
    # task_2 & task_3
    d_to_file = True
    if d_to_file:
        join_files('users.csv', 'hobby.csv', 'save_file.json', d_to_file)
        with open('save_file.json') as f_in:
            print(json.load(f_in))
    else:
        join_files('users.csv', 'hobby.csv', 'users_hobby.txt')
        with open('users_hobby.txt') as f_in:
            print(f_in.read())

    # task_5
    #  python3 task_6_3.py 'users.csv' 'hobby.csv' 'users_hobby.txt'
    join_files(*sys.argv[1:])
# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
#
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками» (не программно); Подумайте о возможных исключительных ситуациях при работе скрипта.
# Усложнение Библиотеки для парсинга yaml использовать нельзя.

import yaml
from os import path

def make_yaml(s_dict, file_name='config.yaml'):
    with open(file_name, 'w') as f_out:
        f_out.write(yaml.dump(s_dict))


def read_yaml(path_to_file='config.yaml'):
    with open(path_to_file) as f_in:
        return yaml.load(f_in, Loader=yaml.FullLoader)


def make_files(s_dict):
    out_path = []
    st = ''
    def req(s_dict, key = None):
        nonlocal st
        if key:
            st += key + '/'
        if isinstance(s_dict, dict):
            for k, v in s_dict.items():
                req(v, k)
                st = f"{'/'.join(st.split('/')[:-2])}/"
        elif isinstance(s_dict, list):
            for v in s_dict:
                req(v)
        else:
            out_path.append(f'{st}{s_dict}'.split('/'))
    req(s_dict)

    for dir in out_path:
        if '.' in dir[-1]:
            if len(dir) > 1:
                full_path = path.join(*dir[:-1])
                if not path.exists(full_path):
                    os.makedirs(full_path)
            open(path.join(*dir), 'w').close()
        else:
            full_path = path.join(*dir)
            if not path.exists(full_path):
                os.makedirs(full_path)


if __name__ == '__main__':
    # d = {'my_project': [
    #     {'settings': [
    #         '__init__.py',
    #         'dev.py',
    #         'prod.py']},
    #     {'mainapp': [
    #         '__init__.py',
    #         'models.py',
    #         'views.py',
    #         {'templates': [
    #             {'mainapp': [
    #                 'base.html',
    #                 'index.html']}]}]},
    #     {'authapp': [
    #         '__init__.py',
    #         'models.py',
    #         'views.py',
    #         {'templates':
    #             {'authapp': [
    #                 'base.html',
    #                 'index.html']}}]}]}
    # make_yaml(d)
    make_files(read_yaml('config.yaml'))
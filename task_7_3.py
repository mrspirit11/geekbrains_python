# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

import os, shutil
from os import path


def unite_folders(path_to='my_project', find_folders_name='templates'):
    find_folders_path = [i[0].split('/') if '/' in i[0] else i[0].split('\\') for i in os.walk(path_to) if i[0].endswith(find_folders_name)]
    for folder in find_folders_path:
        if len(folder) > 2:
            try:
                shutil.copytree(path.join(*folder), path.join(path_to, find_folders_name), dirs_exist_ok=True)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    unite_folders()

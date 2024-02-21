# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование


import logging
from collections import namedtuple
import os
import argparse 


FORMAT = '{asctime} - {msg}'
logging.basicConfig(filename= 'file_list.log', 
                    filemode= 'w', 
                    format= FORMAT,
                    encoding= 'utf-8',
                    level= logging.INFO, style='{')

com_log = logging.getLogger(__name__)
File = namedtuple('File', ['name', 'extension', 'is_directory', 'parent_dir'])

def direct_way(file):
    objects = []
    pars = argparse.ArgumentParser(description= 'gets the path in the console')
    pars.add_argument('file_list', type= str, default= '.', help= 'enter the path to the directory')
    args = pars.parse_args()

    for root, files in os.walk(args.file_list):
        for file in files:
           name, is_directory, extension = os.path.splitext(file)
           parent_dir = root.split('/')[-1]
           file = File(name, extension, is_directory, parent_dir)
           objects.append(file)
           com_log.info(file)

        return objects
    
if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print('Используй: python itog_log.py <directory_path>')
        sys.exit(1)

    directory_path = sys.argv[1]

    files_list = direct_way(directory_path)

    if files_list:
        for file_list in files_list:
            logging.info(f'\n ○ Имя файла: {file_list.name}\n ○ Расширение файла: {file_list.extension}'
                         f'\n ○ Это директория?: {file_list.is_directory}\n ○ Родительская директория: {file_list.parent_dir}')
    else:
        logging.warning('Нет файлов в указанной директории.')

    


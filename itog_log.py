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

FORMAT = '{asctime} - {livelname} - {msg}'
logging.basicConfig(filename= 'list.log', 
                    filemode= 'w', 
                    format= FORMAT,
                    encoding= 'utf-8',
                    level= logging.NOTSET, style='{')

com_log = logging.getLogger(__name__)
File = namedtuple('File',['extension', 'file_name', 'parent_dir'])

def direct_way():
    objects = []
    pars = argparse.ArgumentParser(description= 'gets the path in the console')
    pars.add_argument('file_list', type= str, default= '.', help= 'enter the path to the directory')
    args = pars.parse_args()

    for root, files in os.walk(args.file_list):
        for file in files:
           file_name, extension = os.path.splitext(file)
           parent_dir = root.split('/')[-1]
           file = File(extension, file_name, parent_dir)
           objects.append(file)
           com_log.info(file)

        return objects
    
if __name__ == '__main__':
    print(direct_way())

    


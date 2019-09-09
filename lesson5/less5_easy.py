
__author__ = 'Синицына Наталья Александровна'

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# скрипт создает директории dir_1 - dir_9 в папке, из которой запущен данный скрипт

import os

def createDir1_9():
    i = 1
    while i < 10:
        dirName = 'dir_' + str(i)
        dirPath = os.path.join(os.getcwd(), dirName)
        os.mkdir(dirPath)
        i += 1
# res = createDir1_9()

def createDir():
    dirName = input('Введите имя папки\n')
    dirPath = os.path.join(os.getcwd(), dirName)
    os.mkdir(dirPath)
# res = createDir()

# скрипт удаляет созданные ранеее директории

def deleteDir1_9():
    i = 1
    while i < 10:
        dirName = 'dir_' + str(i)
        dirPath = os.path.join(os.getcwd(), dirName)
        os.rmdir(dirPath)
        i += 1
# res = deleteDir1_9()


def deleteDir():
    dirName = input('Введите имя папки\n')
    dirPath = os.path.join(os.getcwd(), dirName)
    os.rmdir(dirPath)
# res = deleteDir()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def nameDir():
    for itm in os.listdir(os.getcwd()):
        if os.path.isdir(itm):
            print(itm)
# res = nameDir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import sys
import shutil

def copyFile():
    shutil.copy(sys.argv[0], 'less5_easy_copy')
# res = copyFile()
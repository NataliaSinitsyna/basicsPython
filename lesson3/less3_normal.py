
__author__ = 'Синицына Наталья Александровна'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    numberFibn = [1, 1]
    i = 0
    while i <= m:
        numberFibn.append(int(numberFibn[i]) + int(numberFibn[i + 1]))
        i += 1
    return numberFibn[n - 1 : m]
    pass

print(fibonacci(5, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def sort_to_max(origin_list):

    def bubbleSort(list):
        idx = 1
        while idx < len(list):
            for item in range(len(list) - idx):
                if list[item] > list[item + 1]:
                    # list[item + 1] = list[item] + list[item + 1]
                    # list[item] = list[item + 1] - list[item]
                    # list[item + 1] = list[item + 1] - list[item]
                    list[item], list[item + 1] = list[item + 1], list[item]
            idx += 1
        return list

    buff = random.choice(origin_list)
    lessBuff = []
    eqlBuff = []
    moreBuff = []
    i = 0
    while i < len(origin_list):
        for itm in origin_list:
            if itm > buff:
                moreBuff.append(itm)
            elif itm == buff:
                eqlBuff.append(itm)
            else:
                lessBuff.append(itm)
            i += 1

    origin_list = bubbleSort(lessBuff) + eqlBuff + bubbleSort(moreBuff)
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def myFilter(func, sequence):
    import re
    i = 0
    res = []
    while i < len(sequence):
        for itm in sequence:
            if func is not len:            #я не смогла понять как описать условие, когда func is lambda
                if func(itm):
                    res.append(itm)
            else:
                res.append(func(itm))
        i += 1
        return res


print(list(myFilter(lambda x: x > 5, [2, 10, - 10, 8, 2, 0, 14])))
print(list(myFilter(len, ['', 'not null', 'bla', '', '10'])))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def conditionParallelogramm(seq):
    import math
    pointA = []
    pointB = []
    pointC = []
    pointD = []
    res = []
    seqB = []
    seqB.extend(seq)
    seqB.pop(0)
    seqB.pop(0)
    seqB.append(seq[0])
    seqB.append(seq[1])
    seqC = []
    seqC.extend(seqB)
    seqC.pop(0)
    seqC.pop(0)
    seqC.append(seqB[0])
    seqC.append(seqB[1])
    seqD = []
    seqD.extend(seqC)
    seqD.pop(0)
    seqD.pop(0)
    seqD.append(seqC[0])
    seqD.append(seqC[1])
    i = 0
    while i + 3 < len(seq):
        sideA = math.sqrt(((seq[i + 2] - seq[0])**2 + (seq[i + 3] - seq[1])**2))
        pointA.append(sideA)
        sideB = math.sqrt(((seqB[i + 2] - seqB[0])**2 + (seqB[i + 3] - seqB[1])**2))
        pointB.append(sideB)
        sideC = math.sqrt(((seqC[i + 2] - seqC[0]) ** 2 + (seqC[i + 3] - seqC[1]) ** 2))
        pointC.append(sideC)
        sideD = math.sqrt(((seqD[i + 2] - seqD[0]) ** 2 + (seqD[i + 3] - seqD[1]) ** 2))
        pointD.append(sideD)
        i += 2
    idx = 0
    while idx < len(pointB):
        for itm in pointA:
            if itm == pointB[idx]:
                res.append(itm)
        idx += 1
    idx = 0
    while idx < len(pointD):
        for itm in pointC:
            if itm == pointD[idx]:
                res.append(itm)
        idx += 1
    if len(res) >= 4:
        return True
    else:
        return False


print(conditionParallelogramm([-3, 11, 12, -4, 1, 7, -14, 8]))
print(conditionParallelogramm([7, 4, -5, 10, -1, -2, 11, -8]))
print(conditionParallelogramm([0, 0, 0, 6, 6, 8, 2, 6]))
__author__ = 'Синицына Наталья Александровна'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


import random

number = str(random.randint(100, 10000000000))
arr = list(number)
maximum = max(arr)
print(maximum)


# Решение задачи с применением цикла for

import random

number = str(random.randint(100, 10000000000))
maximum = 0
for seq in number:
    if int(seq) > maximum:
        maximum = int(seq)
print(maximum)


# Решение задачи с применением арифметики и цикла while

import random

number = str(random.randint(100, 10000000000))
i = 0
newNumber = str('0')
while i < len(number):
    if int(newNumber) - int(number[i]) < 0:
        newNumber = number[i]
    i += 1
print(newNumber)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.


# Решение с применением синтаксиса кортежей Python

numberOne = tuple(input("Введите первое число \n"))
numberTwo = tuple(input("Введите второе число \n"))
print(numberTwo, numberOne)


# Решение через действия над числами

numberOne = int(input("Введите первое число \n"))
numberTwo = int(input("Введите второе число \n"))
numberTwo = numberOne + numberTwo
numberOne = numberTwo - numberOne
numberTwo = numberTwo - numberOne
print("Первое число = " + str(numberOne) + "\n" + "Второе число = " + str(numberTwo))


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4


import math

print("Программа, вычисляющая корни квадратного уравнения вида ax² + bx + c = 0")
coefficient_a = int(input("Введите коэффициент a \n"))
coefficient_b = int(input("Введите коэффициент b \n"))
coefficient_c = int(input("Введите коэффициент c \n"))
discriminant = (coefficient_b ** 2) - 4 * coefficient_a * coefficient_c
radixOne = str(( - coefficient_b + math.sqrt(discriminant)) / (2 * coefficient_a))
radixTwo = str(( - coefficient_b - math.sqrt(discriminant)) / (2 * coefficient_a))
radixs = print("Первый корень = " + radixOne + "\n" + "Второй корень = " + radixTwo)


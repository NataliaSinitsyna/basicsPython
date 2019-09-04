__author__ = 'Синицына Наталья Александровна'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


#Решение с применением арифметики и цикла while

import random

numberOne = int(random.random() * 100)
numberTwo = int(random.random() * 100)
multiplication = str(numberOne * numberTwo)
i = 0

while i < len(multiplication):
    print(multiplication[i])
    i += 1


#Решение с применением цикла for

import random

print("\n")                                    #разделение результатов первого и второго вариантов кода
numberOne = int(random.random() * 100)
numberTwo = int(random.random() * 100)
multiplication = str(numberOne * numberTwo)

for num in multiplication:
    print(num)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


numberOne = int(input("Введите любое целое число \n"))
numberTwo = int(input("Введите любое целое число \n"))
numberThree = numberOne
numberOne = numberTwo
print(numberOne, numberThree)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"


age = int(input("Введите Ваш возраст \n"))
if age >= 18:
    print("Доступ разрешен \n")
else:
    print("Извините, пользование данным ресурсом только с 18 лет \n")
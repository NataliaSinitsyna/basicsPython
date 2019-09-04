
__author__ = 'Синицына Наталья Александровна'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    numberInt = int(number * (10 ** len(str(number))))
    count = 0
    while len(str(numberInt)) != ndigits:
        numberRes = numberInt % 10
        if numberRes >= 5:
            numberInt = int(numberInt / 10)
            count += 1
            numberInt += 1
        else:
            numberInt = int(numberInt / 10)
            count += 1
    number = numberInt / (10 ** (len(str(number)) - count))
    number = list(str(number))
    while len(number) <= ndigits:
        number.append('0')
    number = ''.join(number)
    return number



print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ticket_number = list(str(ticket_number))
    count = len(ticket_number) // 2
    i = 0
    onePart = int(0)
    twoPart = int(0)
    while i < count:
        onePart += int(str(ticket_number[i]))
        twoPart += int(str(ticket_number[(len(ticket_number) - 1) - i]))
        i += 1
    if onePart == twoPart:
        ticket_number = ''.join(ticket_number)
        return ticket_number


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
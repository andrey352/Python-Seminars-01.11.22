# dz6

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# s = [int(i) for i in input('Input a number: ').split()]
# print(s)
# res = list(filter(lambda x: 9 < x < 100, s))
# print(res)

# 2)

# def double_digit():
#     nums = list(map(int, (input('Input nums: ')).split()))
#     return "".join(map(str, filter(lambda x: 9 < x < 100, nums)))

# print(double_digit())

# ------------------------------------------------------------------------------------------------------------

# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.
#  [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# 1) мой вариант

# list1 = [12, 'sadf', 5643]
# s = [str(i) for i in list1]
# print(s)

# digits = [i for i in s if i.isdigit()]
# letters = list(filter(lambda x: not x.isdigit(), s))
# print(letters)
# print(digits)

# 2)

# lst = [12, 'sadf', 5643]
# lst2 = list(filter(lambda i: type(i) == int, lst))
# lst3 = list(filter(lambda i: type(i) == str, lst))
# print('Numers: ', *lst2)
# print('Strings: ', *lst3)

# -------------------------------------------------------------------------------------------------------------

# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:  6782 -> 23;    0,56 -> 11

# num = input('Input num: ')

# 1) мой вариант
# list1 = [int(i) for i in num if i.isdigit()]
# print(list1)
# print(sum(list1))

# 2)

# def summa(num):
#     return sum(map(int, num.replace('.', '').replace('-', '')))
# num = input('Input num: ')
# print(summa(num))




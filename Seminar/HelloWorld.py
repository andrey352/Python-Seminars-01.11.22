#   Семинар 1

# Зад 1. Прогр, к-я определяет, является ли одно число квадратом дрругого 

# 1)

# a = int(input("Input a: "))                       # или: a, b = int(input()), int(input())
# b = int(input('Input b: '))

# if a**2 == b or b**2 == a:                        # или: if max(a, b) == min(a, b) ** 2:
#     print('a is a squre b')
# else:
#     print('a is not square b')

# --------------------------------------------------------------------------------------------

#  Зад 2. Прогр, к-я находит максимальное число среди пяти введенных

# 1)

# nums = [1, 2, 3, 4, 5]
# max = nums[0]
# for i in nums:
#     if i > max:
#         max = i
# print(f'max number: {max}')

# 2)

# INDEX = 5
# nums = []
# for i in range(0, INDEX):                                                 # или   for i in range(INDEX):
#     nums.append(int(input('Input a number: \n')))
# print(nums)
# print(f'max number: {max(nums)}')

# 3)

# n = int(input('input a number: '))
# nums = [int(input()) for _ in range(n)]                                    # заполнение списка с клав-ры
# max = nums[0]
# for i in range(5):
#     if nums[i] > max:
#         max = nums[i]
# print(max)

# ---------------------------------------------------------------------------------------------------------

#  Зад 3. Прогр, к-я на вход принимает число N, и выводит числа от -N до N

# 1)

# N = int(input('Inpun N: '))                            
# nums = []
# for i in range(-N, N+1):
#     nums.append(i)
# print(nums)

# 2)

# N = int(input('Input N: '))
# nums = [i for i in range(-N, N + 1)]
# print(nums)

# 3)

# n = int(input('Input n: '))
# for i in range(-n, n+1):
#     print(i, end=" ")

#  Зад 2. Прогр, к-я на вход принимает число, и проверяет, кратно ли оно (5 и 10) или 15, но не 30

# n = int(input('Input n: '))
# if ((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and n % 30 != 0:
#     print(True)
# else:
#     print(False)

# ====================================================================================================

#  Семинар 2

# Зад 1. Прогр, к-я будет принимать на вход дробь, и показывать первую цифру дробной части числа
# Пример: 0,5 -> 5, 3 -> нет

# 1)

# num = float(input('Input a number: '))
# if num == round(num, 0):
#     print('incorrect')
# else:
#     print(int(num * 10 % 10))

# 2)

# num = input('Input a number: ')
# if '.' in num:
#     myList = num.split('.')
#     print(myList[1][0])
# else:
#     print('number is not fraction')

# -----------------------------------------------------------------------------------------------

# Зад 2. Даны сумма и произведение чисел. Нужно найти сами ити числа. Пример: 5 6 -> 2 3

# a = int(input('Input sum: '))
# b = int(input('Input a prodact: '))

# 1)

# for x in range(1, a):
#     for y in range(1, a):
#         if x + y == a and x * y == b:
#             print(x, y) 
#             break                               # Не работает, следует поставить флаг, но я не знаю что это 

# 2)

# vvod = input().split()
# s = int(vvod[0])
# p = int(vvod[1])
# for i in range(s + 1):
#     if i * (s - i) == p:
#         print(i, s-i)
#         break












# Зад 2. Прогр, принимает две строки, буква и слово. Прогр должна подсчитать - сколько раз буква
# встречается в слове


# ======================================================================================================

#  Семинар 3. 

# Зад 1. Задайте список. Напишите прогр, к-я определит присутствует ли в данном списке строк некоторое число
# Пример: ['Hello', 'dfhdas', '12', 'uran3']; 2 -> Da, 1 -> Da

# 1)

# a = ["Hello", "dfhdas", "12", "uran3"]
# n = input('Input n: ')
# for i in a:
#     if n in i:
#         print('Da')
#     else:
#         print('No')

# 2)

# s = input().split()
# n = input('Input n: ')
# flag = False
# for i in range(len(s)):
    # if s[i].find(n) > -1:         # find вернет -1 если не найдет строку
#         flag = True
# if flag:
#     print('Da')
# else:
#     print('No')

# 3)

# s = [input() for i in range(5)]
# n = input('Input n: ')
# n = True
# for i in s:
#     if n in i:
#         print('Da')
#         n = False
#         break
# if n:
#     print('number is not found')

# ------------------------------------------------------------------------------------------------

# Зад 2. Прогр, к-я определит позицию второго вхождения строки в списке либо сообщит, что ее нет 
# Пример: ['qwe', 'asd', 'zxc', 'qwe'], ищем 'qwe', ответ: 3

# 1)

# s = ['qwe', 'asd', 'zxc', 'qwe']
# n = input('Input a string: ')
# count = 0
# for i in range(len(s)):
#     if s[i] == n and count == 1:
#         print(i)
#     if s[i] == n and count == 0:
#         count += 1

# 2)

# s = ['qwe', 'asd', 'zxc', 'qwe']
# n = input('Input a string: ')
# if s.count(n) < 2:
#     print("There is not second entering")
# else:
#     s.remove(n)                                  # удаляет первое вхождение
#     print(s.index(n) + 1)

# -------------------------------------------------------------------------------------------------------

# Зад 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора
#  псевдослучайных чисел

# import time

# def get_rand(x, y):
#     scope = y - x
#     print(time.time())
#     result = int(time.time())%scope
#     return result + x

# print(get_rand(80, 100))

# =====================================================================================================

#   Семинар 4

# Зад 1. Задайте строку из чисел. Напишите прогр, к-я покажет большее и меньшее число. Разделитель - пробел.

# map(функция, набор значений)

# s = [int(i) for i in input('Input numbers: ').split()]
# s = list(map(int, input().split()))                         # второй вариант списка
# print(max(s), min(s))



# ----------------------------------------------------------------------------------------------------

# Зад 2. Найдите корни квадратного уравнения  Ax² + Bx + C = 0 двумя способами
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = b**2 - 4*a*c

# if d > 0:
#     x1 = (-b + d**0.5) / (2*a)
#     x2 = (-b - d**0.5) / (2*a)
#     print('x1 = ', x1)
#     print('x2 = ', x2)
# elif d == 0:
#     x1 = -b / (2*a)
#     print('x1 = ', x1)
# else:
#     print('корней нет')

# -------------------------------------------------------------------------------------------------

# 3. Задайте два числа. Напишите прогр, к-я найдёт НОК (наименьшее общее кратное) этих двух чисел.
# Пример: Ввод: 3 5 Вывод: 15;   Ввод: 13 39  Вывод: 39
# нок(а, в) = а*в/нод(а, в)

# 1)

# a = int(input('a = '))
# b = int(input('b = '))

# nod = 1
# for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         nod = i
# nok = a*b/nod
# print(nok)

# 2)

# a = int(input())
# b = int(input())
# for i in range(2, a*b + 1):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break





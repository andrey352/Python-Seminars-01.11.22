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

# =======================================================================================================

#      Семинар 5

# Зад 1. 1. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: 1 2 3 5 6 -> 4

# path = 'file.txt'                       # or path = C:\Users\Uzver\Desktop\Seminar Python\Seminar\file.txt
# data = open(path, 'r')                  # or with open('file.txt') as file:
# string = data.read()                                data = file.readline()
# data.close()
# s = [int(i) for i in string.split()]
# print(s)
# for i in range(1, len(s) - 1):
#     if s[i+1] != s[i] + 1:
#         print(s[i] + 1)
        
# ------------------------------------------------------------------------------------------------------

#  Зад 2. Напишите программу, удаляющую из текста все слова, содержащие "абв".Строка находится в файле.
# Пример: ывпвап вапапро приветабв привет приветаб -> ывпвап вапапро привет приветаб

# 1)

# path = 'new.txt'
# data = open(path, 'r', encoding='UTF-8')                 # если русские буквы то исп-ем encoding='UTF-8'
# str = data.read()
# data.close()
# s = str.split()                                          # скобки не нужны т к .split() и так возвращает список
# print(s)
# s1 = list(filter(lambda x: not 'абв' in x, s))           
# print(s1)

# 2)

# with open('new.txt', encoding='UTF-8') as file:
#     data = file.readline()
# print(data)
# data = [i for i in data.split() if 'абв' not in i]
# print(' '.join(data))

# -------------------------------------------------------------------------------------------------------

#  Зад 3. **Доп** Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую 
# последовательность. Порядок элементов менять нельзя.
# *Пример:* [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# 1)

# from random import randint
# s = [1, 5, 2, 3, 4, 6, 1, 7]
# m = []
# t = randint(0, len(s)-1)
# m.append(min(s))
# for i in range(1, len(s) ):
#     if s[i] > m[-1]:
#         m.append(s[i])
# print(m) 

# =====================================================================================================

#    Семинар 6

# Зад 1. Напишите прогр вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
# приоритет операций стандартный.
# Пример: 2+2 => 4;  1+2*3 => 7;  1-2*3 => -5;
# Доп: - Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:  1+2*3 => 7;   (1+2)*3 => 9;

# sent = [i for i in input('Input exp: ').split()]
# print(sent)
# components = [int(i) if i.isdigit() else i for i in sent]
# print(components)
# result = 0
# while '*' in components:
#     i = components.index('*')
#     result = components[i - 1] * components[i + 1]
#     components = components[:i - 1] + [result] + components[i + 2:]
# while '/' in components:
#     i = components.index('/')
#     result = components[i - 1] / components[i + 1]
#     components = components[:i - 1] + [result] + components[i + 2:]
# while '+' in components:
#     i = components.index('+')
#     result = components[i - 1] + components[i + 1]
#     components = components[:i - 1] + [result] + components[i + 2:]
# while '-' in components:
#     i = components.index('-')
#     result = components[i - 1] - components[i + 1]
#     components = components[:i - 1] + [result] + components[i + 2:]
# print(components)

# ---------------------------------------------------------------------------------------------------

# Зад 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#  Без использования Count()
# Пример:  [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# 1)

# from random import randrange

# quantity = 10
# s = [randrange(7) for i in range(quantity)]
# print(s)
# p = []
# for i in s:
#     b = 0
#     for k in s:
#         if i == k:
#             b += 1
#     if b == 1:
#         p.append(i)
# print(*p)

# 2)

# def find_unique(data):
#     res = []
#     res_new = []
#     for el in data:
#         if el not in res and el not in res_new:
#             res.append(el)
#             res_new.append(el)
#         elif el in res:
#             res.remove(el)
#     print(res_new)
#     return sorted(res)

# secuence = [1, 1, 1,  2, 2, 3, 10]

# print('исходная последовательность: ', secuence)
# print('Отсортированный список уникальных эл-тов ', find_unique(secuence))

# ====================================================================================================

#   Семинар 7

#  Мы протто рисовали диаграмму разбиения на файлы логики программы. (интерфейс, учитель, ученик, логер)

# =====================================================================================================

















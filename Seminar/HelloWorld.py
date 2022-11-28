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



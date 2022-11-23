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












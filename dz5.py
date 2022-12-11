# dz 5

# Зад 1. 1) Создайте прогр для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# 2021 21 ---> 2000 бот 4 -> 1996 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота


# from random import randint
# num = 120
# print('Число конфет которое нужно взять 1м ходом для победы - ', num % 29)
# while num > 0:
#     x = int(input('Игрок 1. Возьму конфет: '))
#     num = num - x
#     print('осталось ', num , ' конфет')
#     if num == 0:
#         print('Игрок 1 победил')
#         break
#     else:
#         print()
#         if num < 28:
#             print('Бот взял ', num, ' конфет и победил')
#             break
#         else:
#             y = int(randint(1, 28))
#             print('Бот взял ', y , ' конфет')
#             num = num - y
#             print('осталось ', num , ' конфет')
#             print('Для победы нужно взять ', (29 - y), 'конфет')
#             print()

# ----------------------------------------------------------------------------------------------

# Зад 2. Создайте программу для игры в ""Крестики-нолики"".

# board = list(range(1,10))
# def draw_board(board):
#     print('-' * 13)
#     for i in range(3):
#         print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3])
#         print('-' * 13)

# def take_input(player_token):                                          # проверяет правильность ввода пользователя
#     valid = False
#     while not valid:
#         player_answer = input('Куда поставим: ' + player_token + '? ')

#         try:
#             player_answer = int(player_answer)
#         except:
#             print('Нужно ввести число!')
#             continue                                                    # продолжать если не ввели число
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer - 1]) not in 'XO'):
#                 board[player_answer - 1] = player_token
#                 valid = True
#             else:
#                 print('Эта клетка уже занята')
#         else:
#             print('Введите число от 1 до 9')

# def check_win(board):                                                   # проверяет выйграл ли игрок
#     win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input('X')
#         else:
#             take_input('O')
#         counter += 1

#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, 'Ты выйграл')
#                 win = True
#                 break
#         if counter == 9:
#             print('Ничья')
#             break
#     draw_board(board)
# main(board)

# --------------------------------------------------------------------------------------------

# Зад 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# "aaabbbbccbbb" -> "3a4b2c3b"
# "3a4b2c3b" -> "aaabbbbccbbb"

# with open('C:/Users/Uzver/Desktop/Seminar Python/file2.txt') as file:
#     data = file.readline()
# print(data)
# s = list(data)

# def coding(s):
#     if len(s) < 1:
#         return ""
#     count = 0
#     el = s[0]
#     result = ""
#     for elem in s:
#         if elem == el:
#             count += 1
#         else:
#             result += str(count) + el 
#             count = 1
#             el = elem
#     else:
#         result += str(count) + el 
#     return result

# print(coding(s))

# def decoding(s):
#     if len(s) < 1:
#         return ""
#     num = ""
#     result = ""
#     for elem in s:
#         if elem.isdigit():
#             num += elem
#         else:
#             for i in range(int(num)):
#                 result += elem
#             else:
#                 num = ""
#     return result

# print(decoding(coding(s)))













import digit, in_num, log

def button_click():
    print('Введите "0" если хотите продолжить')
    print('Введите "1" если хотите закончить')
    flag = int(input())
    while flag == 0:
        primer = digit.parse()                     # [1, '+', 3, '*', 5]
        result = digit.calculate(primer)           # 7
        in_num.view_data(result)                   # показывает рез-т
        log.loger(primer, result)
        print('Введите "0" если хотите продолжить')
        print('Введите "1" если хотите закончить')
        flag = int(input())
    print('Программа завершилась. Удачи!')


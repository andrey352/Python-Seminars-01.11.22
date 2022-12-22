from model import get_info
from logger import writing_csv, read_contact, writing_txt 


def ui_start():
    while True:
        print('выберите режим работы со справочником: ')
        print('1. Записать нового абонента\n2. Вывести справочник на экран\n3. Выход из программы')
        mode = int(input())
        if mode == 1:
            a = get_info()
            writing_txt(a)
            writing_csv(a)
        elif mode == 2:
            print(read_contact())
        elif mode == 3:
            print('Выход из программы')
            break

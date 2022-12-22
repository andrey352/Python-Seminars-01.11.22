from student_database import load_db, save_db
from student import see_rating
from teacher import add_student, put_rating



def controller():
    load_db()
    match input('Укажите себя. 1 - учитель, 2 - ученик: '):
        case '1':
            flag = 1
            while flag == 1:
                print('Что нужно сделать?')
                act = input('1 - Записать ученика, 2 - Выставить оценку, 0 - Выйти из программы\nВвод: ')
                if act == '1':
                    add_student()
                elif act == '2':
                    put_rating()
                elif act == '0':
                    flag = 0
            else:
                save_db()                   # сохранение данных в файл db_students.json
        case '2':
            flag = 1
            while flag == 1:
                last_name = input("Введите фамилию ученика или '0' для выхода из программы\nВвод: ")
                if last_name == '0':
                    flag = 0                                           # Как только введем 0 - программа выйдет
                else:
                    see_rating(last_name)

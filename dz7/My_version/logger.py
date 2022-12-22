
def read_contact():
    with open('phonebook.csv', 'r', encoding='utf-8') as f:
        return f.read()

def writing_csv(info):
    file = 'phonebook.csv'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}; Имя: {info[1]}; Телефон: {info[2]}\n')

def writing_txt(info):
    file = 'phonebook.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nТелефон: {info[2]}\n\n')



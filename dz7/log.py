def loger(dir):
    with open('file.txt', 'a') as data:
        rec = dir + ';\n'
        data.writelines(rec)


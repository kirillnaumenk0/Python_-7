from File_writing import writing_csv as wrc
from File_writing import reading_csv as rec

def choice():
    print('Выберите дейстиве \n 1: Запись контакта \n 2: Просмотр контактов')
    choices = input("Ввод: ")
    if choices == '1':
        wrc()
    elif choices == '2':
        rec()
    elif choices != '1' or '2':
        print('Error')        

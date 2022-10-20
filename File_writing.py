import csv


def write_phone_book():
    surnames = []
    names = []
    phones = []
    comments = []
    while True:
        surname = input('Введите фамилию, или команду (end) для завершения ')
        if surname == 'end':
            break
        name = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        comment = input('Введите коментарий: ')
        surnames.append(surname)
        names.append(name)
        phones.append(phone)
        comments.append(comment)

    phones_book = {}
    for i in range(len(surnames)):
        key = i + 1
        phones_book[key] = []
        phones_book[key].append(surnames[i])
        phones_book[key].append(names[i])
        phones_book[key].append(phones[i])
        phones_book[key].append(comments[i])
    return phones_book


book = write_phone_book()

def writing_csv():
    with open("data1.csv", "a", newline='') as file:
        for value in book.values():
            writer = csv.writer(file, delimiter=';', quotechar='"')
            writer.writerow(value)


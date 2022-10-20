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
    
    phone_book = {}
    for i in range(len(surnames)):
        key = i + 1
        phone_book[key] = []
        phone_book[key].append(surnames(i))
        phone_book[key].append(names(i))
        phone_book[key].append(phones(i))
        phone_book[key].append(comments(i))
    return phone_book

write_phone_book()
import csv

phone_book = [
    "Surname", "Name", "Phone", "Comments"
]


def creating_cap():
    with open("data1.csv", "w") as file:
        write = csv.writer(file, delimiter=";")
        write.writerow(phone_book)
    




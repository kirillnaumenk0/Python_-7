from CSV_creating import creating as cr
from os import path

def check(text = "data1.csv"):
    if path.exists(text):
        with open("data1") as file:
            print('openning')
    else:
        print('error')

check()
import random

import dbmanager
SYMBOLS = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]+[i for i in range(10)]+['!','@','#','$','%','^','&','*']
LEN = 10


class Note(object):
    def __init__(self, place):
        self.place = place
    def gen_raw_data(self):
        self.raw_data = [random.choice(range(len(SYMBOLS)+1)) for i in range(LEN+1)]
    def get_data(self, key, data):
        #key = input('key? ')
        for i in range(LEN+1):
            d = data[i]+ord[key[i]]
            if d > len(SYMBOLS):
                d =- len(SYMBOLS)
            print(SYMBOLS[d], end='')

if __name__ == '__main__':
    while True:
        place = input('Добро пожаловать! Введите название учетки: ')
        if place == 'exit':
            break
        if place == 'start':
            dbmanager.DBManager.create('pass', 'id integer', 'site text', 'pas char(16)')

        if not dbmanager.DBManager.search('pass', 'site', place):
            dbmanager.DBManager.insert('pass', site=place, pas=Note.get_raw_())
            dbmanager.DBManager.commit()

        key = input('Введите ключ: ')
        pas = dbmanager.DBManager.search('pass', 'site', place)
        print(pas)

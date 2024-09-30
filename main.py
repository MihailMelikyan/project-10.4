import queue # позволяет работать с очередями
import threading # работа с потоками
from queue import Queue
from time import sleep
from random import randint

class Table:
    def __init__(self,number):
        self.number = number # номер стола
        self.guest = None # изначально пустая используется для хранения гостя сидящего за столом
class Guest:
    threading.Thread()
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self): # переопределенный метод который симулирует процесс еды
        sleep(randint(3, 10)) # гость делает паузу

class Cafe:
    def __init__(self,*tables):
        self.queue = Queue() #создаем очередь для гостей
        self.tables = tables # список столов который хранит переданные столы

    def guest_arrival(self,*guests): # метод принимающий гостей кафе
        for guest in guests:
            for table in self.tables:
                if table.guest is None: # если стол свободен
                    guests.start() # запускаем поток для гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest  # Закрепляем гостя за столом.
                    break  # Прерываем цикл, т.к. гость сел за стол.
                else:
                    print(f'{guest.name} в очереди')
                    self.queue.put(guest)  # Добавляем гостя в очередь.

    def discuss_guests(self):
        while  self.queue.empty() == False or any([table.guest for table in self.tables]):
            for table in self.tables:
                if not table.guest.is_alive():
                    print(f'{guest.name} покушал(-а) и ушёл(ушла) Стол номер "{table.number}" свободен')
                    table.guest = None
                else:




            













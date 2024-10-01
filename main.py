import queue  # позволяет работать с очередями
import threading # работа с потоками

from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number  # номер стола
        self.guest = None  # изначально пустая используется для хранения гостя сидящего за столом


class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):  # переопределенный метод который симулирует процесс еды
        sleep(randint(3, 10))  # гость делает паузу


class Cafe:
    def __init__(self, *tables):
        self.tables = []
        self.queue = Queue()  # создаем очередь для гостей
        for table in tables:
            self.tables.append(table)  # список столов который хранит переданные столы


    def guest_arrival(self, *guests):  # метод принимающий гостей в кафе
        for guest in guests:
            seated = False  # Флаг, указывающий, что гость был размещен
            for table in self.tables:
                if table.guest is None:  # если стол свободен
                    table.guest = guest  # Закрепляем гостя за столом.
                    guest.start()  # запускаем поток для гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    seated = True  # Устанавливаем флаг в True, так как гость сел
                    break  # Прерываем цикл, т.к. гость сел за стол.

            if not seated:  # Если после проверки всех столов гость не был размещен
                print(f'{guest.name} в очереди')  # Сообщаем, что гость ждет
                self.queue.put(guest)  # Добавляем гостя в очередь.

    def discuss_guests(self):
        while self.queue.empty() == False or any([table.guest for table in self.tables]):
            for table in self.tables:
                if not table.guest is None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла) \nСтол номер "{table.number}" свободен')
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} занял стол номер "{table.number}" ')
                        else:
                            table.guest = None
        print("обслуживание завершено")


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Мария', 'Олег', 'Вахтанг', 'Сергей', 'Дарья', 'Арман', 'Виктория', 'Никита', 'Павел', 'Илья', 'Александр']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
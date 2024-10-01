import queue  # позволяет работать с очередями
import threading  # работа с потоками

from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number  # номер стола
        self.guest = None  # изначально пустая используется для хранения гостя сидящего за столом


class Guest(threading.Thread):
    def __init__(self, name):
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
        while not (self._all_table_free() and self.queue.empty()):
            for number, table in self.tables.items():
                if not table.guest is None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла) \nСтол номер "{table.number}" свободен')
                        if not self.queue.empty():
                            self.tables[number].guest = self.queue.get()
                            self.tables[number].guest.start()
                        # после окончания потока гостя, нужно заменить гостя и запустить его поток
                        # пока в очереди есть гость, нужно заменять гостей на гостей и запускать их потоки
                        # как только гости в очереди закончатся, можно заменять гостя на None
                        # цикл закончится когда очередь будет пуста а все гости за столами будут None

                        print(f'{table.guest} вышел(-шла) из очереди и сел(-ла) за стол номер "{number}"')

                        # проверка пуста ли очередь, если пуста то заменить ушедшего гостя на None,
                        # если нет то посадить гостя за стол

                    else:
                        self.tables[n].guest = None


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Мария', 'Олег', 'Вахтанг', 'Сергей', 'Дарья', 'Арман', 'Виктория', 'Никита', 'Павел', 'Илья',
                'Александр']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

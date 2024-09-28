from threading import Thread
import threading
from random import randint
from time import sleep
import queue

class Table():
    def __init__(self,number,guest = None):
        self.number = number

class Guest(Thread):
    def __init__(self,name):
        self.name = name
    def run(self):
        exep = randint(3,10)


class Cafe(Table):
    def __init__(self,table,queue):
        self.table = []
        self.queue = queue


    def guest_arrival(self,*guests):



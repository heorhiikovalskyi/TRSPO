# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import time
import random
class First:
    def __init__(self, value):
        self.value = value
        self.mutex = threading.Lock()
    def read(self):
        return self.value
    def write(self, term):
        self.mutex.acquire()
        self.value += term
        self.mutex.release()

class Second:
    def __init__(self, value):
        self.value = value
        self.mutex = threading.Lock()
    def read(self):
        return self.value
    def write(self, term):
        self.mutex.acquire()
        self.value += term
        self.mutex.release()

first_obj = First(0)
second_obj = Second(0)

def increase(K):
    for i in range(K):
        first_obj.write(random.uniform(10.5, 75.5))
        second_obj.write(random.uniform(10.5, 75.5))

count = random.randint(10,20)
threads = []
K1 = random.randint(10000, 20000)
K2 = random.randint(10000, 20000)

for i in range(count//2):
    threads.append(threading.Thread(target = increase, args = (K1,)))

for i in range(count//2):
    threads.append(threading.Thread(target = increase, args = (K2,)))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(time.time() - start)


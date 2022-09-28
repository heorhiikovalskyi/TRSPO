import threading
import time
import random

mutex1 = threading.Lock()
mutex2 = threading.Lock()


class Value:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value

    def write(self, term):
        self.value += term


first_obj = Value(0)
second_obj = Value(0)


def increase1(K):
    for i in range(K):
        mutex1.acquire()
        try:
            first_obj.write(random.uniform(10.5, 75.5))
        finally:
            mutex1.release()
        mutex2.acquire()
        try:
            second_obj.write(random.uniform(10.5, 75.5))
        finally:
            mutex2.release()

def increase2(K):
    for i in range(K):
        mutex1.acquire()
        try:
            second_obj.write(random.uniform(10.5, 75.5))
        finally:
            mutex1.release()
        mutex2.acquire()
        try:
            first_obj.write(random.uniform(10.5, 75.5))
        finally:
            mutex2.release()

count = random.randint(10, 20)
threads = []
K1 = random.randint(10000, 20000)
K2 = random.randint(10000, 20000)

for i in range(count // 2):
    threads.append(threading.Thread(target=increase1, args=(K1,)))

for i in range(count // 2):
    threads.append(threading.Thread(target=increase2, args=(K2,)))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(time.time() - start)


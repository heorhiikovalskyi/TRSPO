N = 10000
from queue import Queue
import threading
import time
q = Queue()
result = []
mutex1 = threading.Lock()

def Foo():
    while 1 == 1:
        print('start')
        if len(result) == N:
            break
        element = q.get()
        if element.evolution == 1:
            mutex1.acquire()
            result.append(element)
            mutex1.release()
        else:
            if element.evolution % 2 == 0:
                element.evolution = int(element.evolution / 2)
            else:
                element.evolution = int(3 * element.evolution + 1)
            element.count += 1
            q.put(element)

class Node:
    def __init__(self, value):
        self.value = value
        self.count = 0
        self.evolution = value

for i in range(1, N + 1):
    q.put(item = Node(i))

threads = []

for i in range(12):
    threads.append(threading.Thread(target=Foo, args=()))
start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(time.time() - start)


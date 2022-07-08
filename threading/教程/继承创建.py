import time
import random
import threading


class Func(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        s = random.randint(1, 5)
        print(f'current thread is {self.name}, sleeping {s}s.')
        time.sleep(s)
        print(f'thread {self.name} is over')


if __name__ == '__main__':
    for i in range(1, 5):
        t = Func(str(i))
        t.start()
    print('Main Thread')
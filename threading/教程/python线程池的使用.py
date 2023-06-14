import time
import random
from concurrent.futures import ThreadPoolExecutor


def func(name):
    s = random.randint(1, 5)
    print(f'current thread is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'thread {name} is over')


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as t:
        for i in range(1, 6):
            t.submit(func, i)
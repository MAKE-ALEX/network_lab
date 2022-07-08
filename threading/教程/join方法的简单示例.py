import time
import random
import threading


def func(name):
    s = random.randint(1, 5)
    print(f'current thread is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'thread {name} is over')


if __name__ == '__main__':
    print('Main Thread start')
    tlist = []
    for i in range(1, 5):
        t = threading.Thread(target=func, args=(i,))
        t.start()
        tlist.append(t)
    for t in tlist:
        t.join()
    print('do something')
    print('Main Thread over')


"""
Main Thread start
current thread is 1, sleeping 4s.
current thread is 2, sleeping 4s.
current thread is 3, sleeping 2s.
current thread is 4, sleeping 5s.
thread 3 is over
thread 1 is overthread 2 is over

thread 4 is over
do something
Main Thread over

进程已结束,退出代码0
"""
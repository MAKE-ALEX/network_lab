import time
import random
import threading

# https://www.cnblogs.com/blueberry-mint/p/13722871.html
# 上面例子开启了4个线程，4个线程并发执行任务，先完成任务的线程先输出结果。
def func(name):
    s = random.randint(1, 5)
    print(f'current thread is {name}, sleeping {s}s.')
    time.sleep(s)
    print(f'thread {name} is over')


if __name__ == '__main__':
    for i in range(1, 5):
        t = threading.Thread(target=func, args=(i,))
        t.start()
    print('Main Thread')

"""
current thread is 1, sleeping 5s.
current thread is 2, sleeping 3s.
current thread is 3, sleeping 1s.
current thread is 4, sleeping 1s.Main Thread

thread 3 is over
thread 4 is over
thread 2 is over
thread 1 is over

进程已结束,退出代码0
"""

import time

timer_list = []


def timer(any_func):
    def wrapper_func():
        time1 = time.time()
        any_func()
        time2 = time.time()
        timer_list. append(time2 - time1)
    return wrapper_func


@timer
def fast_function():
    for i in range(1000000):
        print(i * i, flush=True)
@timer
def slow_function():
    for i in range(10000000):
        print(i * i , flush=True)

fast_function()
slow_function()
print(timer_list)
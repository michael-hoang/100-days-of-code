import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(decorated_func):
    def wrapper():
        t1 = time.time()
        decorated_func()
        t2 = time.time()
        print(f'{decorated_func.__name__} run speed: {t2-t1}')

    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
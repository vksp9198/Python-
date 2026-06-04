# Problem : Implement a decorator that caches the return values of a function when it's called the same arguments , the cached value is returned instead of re-executing the function.
import time 


def my_decorator(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@my_decorator
def long_running_function(a,b):
    time.sleep(4)
    return a+b
print(long_running_function(6,7))
print(long_running_function(6,7))
print(long_running_function(6,7))
print(long_running_function(6,9))

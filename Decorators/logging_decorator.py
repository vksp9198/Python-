from functools import wraps

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args ,**kwargs)
        print(f"Returned = {result}")
        return result
    return wrapper

@log_function
def square(a):
    # print(f"Square : {a*a}")
    return a * a

square(4)
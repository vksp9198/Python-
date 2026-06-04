def my_decorator(func):
    def wrapper(*args):
        print(func.__name__,"function")
        return func(*args)
    return wrapper

@my_decorator
def add(*args):
    return sum(args)
print(add(9,6))
print(add(9,6,4,5,6))
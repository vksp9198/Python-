# Decorators : A Decorator is a function that takes
# another function as an argument and returns a new function.

def my_decorator(func):
    def wrapper():
        print("before function execution!")
        func()
        print("after function execution!")
    return wrapper
    
@my_decorator
def greet():
    print("hello!")
greet()
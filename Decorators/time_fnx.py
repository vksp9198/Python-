# Time Function Execution: Write a decorator that measure the time a function takes to execute 
import time

def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        result = func(*args , **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
example_function(5)



def username(func):
    def wrapper(*args):
        print(f"{func.__name__}")
        return func(*args)
    return wrapper

@username
def userData(id, name , age):
    print(f"Id : {id}")
    print(f"Name : {name}")
    print(f"Age : {age}")
userData(117 , "Vikas Prajapati", 19)
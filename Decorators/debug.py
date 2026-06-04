# decorator for greet_user 
def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(str(f"{key} : {value}") for key, value in kwargs.items())
        print(f" {args_value} , {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper





@debug
def greet_user(name , greet = "Hello!"):
    print(f"{greet}, {name}")
greet_user("Vikas Prajapati")
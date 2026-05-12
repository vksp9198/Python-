# Problem: Create a function that accept of keyword arguments and prints then in the formate string. [funtion with **kwargs]

def print_kwargs(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name = "Vikas", age = 19)
print_kwargs(address = "Ghansoli", state = "Navi Mumbai")
print_kwargs(mobile = 9198776636)

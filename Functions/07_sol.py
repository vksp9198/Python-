# problem: write a function that takes a variable of arguments and print thier sum 

def sum_of_arguments(*arg):
    return sum(arg)
print(sum_of_arguments(1,2,3,4))
print(sum_of_arguments(1,2,3,4,5,6,7,8))
print(sum_of_arguments(1,2,3,4,5,6,7,8,9,10))
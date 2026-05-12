# Problem : recursion function to calculate the factorial of given number 

def factorial(n):
    if n == 0 :
        return 1
    else: 
        return n * factorial(n - 1)

print("factorial is = ", factorial(5)) 

# Problem : Find the factorial of a given number (5) using while loop 

number = int(input("Enter any number: "))
factorial = 1

while number > 0:
    # factorial = factorial * number
    factorial *= number
    number -= 1

print("factorial is  =" , factorial)



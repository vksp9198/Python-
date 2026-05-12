# Problem : check the given number is pirme number or not and print the result.is_prime. 
userInput = int(input("Enter any number : "))
is_prime = True

if userInput > 1:
    for i in range(2, userInput):
        if(userInput % i) == 0:
            is_prime = False
            break
print(is_prime)

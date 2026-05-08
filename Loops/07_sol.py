# Problem: Validate input = Keep asking the user for input until they enter a number between  1 to 10. 

while True:
    number = int(input("Enter number between 1 to 10 = "))
    if 0 <= number <= 10: 
        print("Thanks!!")
        break
    print("Invalid number!! , Try again.")

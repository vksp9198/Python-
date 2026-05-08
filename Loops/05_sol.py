# Problem : Find the first non-repeated character in a string 

username = "Vikas"

for char in username:
    #print(char)     #it shows characters too.
    if username.count(char) == 1:
        print("First non-repeated character is : ",char)
        break

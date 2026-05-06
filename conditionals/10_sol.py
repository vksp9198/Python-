pet = "cat"
year = 9 
food = "puppy food"
 
if pet == "dog":
    if year < 2:
        food = "Puppy food"
elif pet == "cat":
    if year > 5 :
        food = "Senior food"
print("food for" , pet, "is" , food)
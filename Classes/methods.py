# Problem: Add a method to the Car class that displays the full name of car(brand and name)
class Car:
    def __init__(self , brand , model):
        self.brand = brand                   
        self.model = model
    
    
    def full_name_of_car(self):
        return f"{self.brand} {self.model}"
        
       

# I - instance of Car 
myCar = Car("Toyota" , "Innova Crysta")
print(myCar.brand)
print(myCar.model)
print(myCar.full_name_of_car())

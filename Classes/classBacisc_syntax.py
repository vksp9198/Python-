# Problem: Create a Car class with attributes like brand and model. then create an instance of this class 

class Car:
       def __init__(self , brand , model):
            self.brand = brand                   
            self.model = model
       

myCar = Car("Maruti suzuki" , "swift")  # It's called an instance of a class.

print(myCar.brand)
print(myCar.model)

# II - instance of Car 
myCar2 = Car("Tata" , "Nexon")
print(myCar2.brand)
print(myCar2.model)


# III - instance of Car 
myCar3 = Car("Mahindra" , "Thar")
print(myCar3.brand)
print(myCar3.model)

# IV - instance of Car 
myCar4 = Car("Toyota" , "Innova Crysta")
print(myCar4.brand)
print(myCar4.model)

# V - instance of Car 
myCar4 = Car("Honda", "City")
print(myCar4.brand)
print(myCar4.model)
# Problem: Create a ElectricCar class that inherit from car and has an additional attributes battery_size:
class Car:
    def __init__(self , brand , model):
            self.brand = brand                   
            self.model = model
        
class ElectricCar(Car):
     def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)

        self.battery_size = battery_size
     
# I - instance of Car 
my_electric_car = ElectricCar("Toyota" , "Innova Crysta" , "40.43kwh")
print(my_electric_car.brand)
print(my_electric_car.model)
print(my_electric_car.battery_size)

